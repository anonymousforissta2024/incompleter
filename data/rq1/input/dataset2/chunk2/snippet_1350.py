#Source: https://stackoverflow.com/questions/72084680/typeerror-keyword-argument-not-understood-query-shape-with-keras-and-te
class ShiftedPatchTokenization(layers.Layer):
    def __init__(
      self,
      image_size=IMAGE_SIZE,
      patch_size=PATCH_SIZE,
      half_patch=PATCH_SIZE//2,
      num_patches=NUM_PATCHES,
      projection_dim=PROJECTION_DIM,
      flatten_patches=None,
      projection=None,
      layer_norm=None,
      vanilla=False,
      **kwargs,
    ):
      super(ShiftedPatchTokenization,self).__init__(**kwargs)
      self.vanilla = vanilla  # Flag to switch to vanilla patch extractor      
      self.image_size = image_size
      self.patch_size = patch_size
      self.half_patch = patch_size // 2 # la divisione con // dà il numero in int()
      self.flatten_patches = layers.Reshape((num_patches, -1))
      self.projection = layers.Dense(units=projection_dim)
      self.layer_norm = layers.LayerNormalization(epsilon=LAYER_NORM_EPS)

    # Override function to avoid error while saving model
    def get_config(self):
      config = super().get_config().copy()
      config.update(
          {
          "image_size": self.image_size,
          "patch_size": self.patch_size,
          "half_patch": self.half_patch,
          "flatten_patches": self.flatten_patches,
          "vanilla": self.vanilla,
          "projection": self.projection,
          "layer_norm": self.layer_norm,
          }
      )
      return config
     


    @classmethod
    def from_config(cls, config):
        return cls(**config)

    def crop_shift_pad(self, images, mode):
        # Build the diagonally shifted images
        if mode == "left-up":
            crop_height = self.half_patch
            crop_width = self.half_patch
            shift_height = 0
            shift_width = 0
        elif mode == "left-down":
            crop_height = 0
            crop_width = self.half_patch
            shift_height = self.half_patch
            shift_width = 0
        elif mode == "right-up":
            crop_height = self.half_patch
            crop_width = 0
            shift_height = 0
            shift_width = self.half_patch
        else:
            crop_height = 0
            crop_width = 0
            shift_height = self.half_patch
            shift_width = self.half_patch

        # Crop the shifted images and pad them
        crop = tf.image.crop_to_bounding_box(
            images,
            offset_height=crop_height,
            offset_width=crop_width,
            target_height=self.image_size - self.half_patch,
            target_width=self.image_size - self.half_patch,
        )
        shift_pad = tf.image.pad_to_bounding_box(
            crop,
            offset_height=shift_height,
            offset_width=shift_width,
            target_height=self.image_size,
            target_width=self.image_size,
        )
        return shift_pad

    def call(self, images):
        if not self.vanilla:
            # Concat the shifted images with the original image
            images = tf.concat(
                [
                    images,
                    self.crop_shift_pad(images, mode="left-up"),
                    self.crop_shift_pad(images, mode="left-down"),
                    self.crop_shift_pad(images, mode="right-up"),
                    self.crop_shift_pad(images, mode="right-down"),
                ],
                axis=-1,
            )
        # Patchify the images and flatten it
        patches = tf.image.extract_patches(
            images=images,
            sizes=[1, self.patch_size, self.patch_size, 1],
            strides=[1, self.patch_size, self.patch_size, 1],
            rates=[1, 1, 1, 1],
            padding="VALID",
        )
        flat_patches = self.flatten_patches(patches)
        if not self.vanilla:
            # Layer normalize the flat patches and linearly project it
            tokens = self.layer_norm(flat_patches)
            tokens = self.projection(tokens)
        else:
            # Linearly project the flat patches
            tokens = self.projection(flat_patches)
        return (tokens, patches)


class PatchEncoder(layers.Layer):
    def __init__(
        self,
        num_patches=NUM_PATCHES,
        projection_dim=PROJECTION_DIM,
        position_embedding=None,
        positions=None,
        **kwargs
    ):
        super(PatchEncoder,self).__init__(**kwargs)
        self.num_patches = num_patches
        self.position_embedding = layers.Embedding(
            input_dim=num_patches, output_dim=projection_dim
        )
        self.positions = tf.range(start=0, limit=self.num_patches, delta=1)

    def get_config(self):
      config = super().get_config().copy()
      config.update({
          "num_patches": self.num_patches,
          "position_embedding": self.position_embedding,
          "positions": self.positions.numpy(),
      })
      return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)

    def call(self, encoded_patches):
        encoded_positions = self.position_embedding(self.positions)
        encoded_patches = encoded_patches + encoded_positions
        return encoded_patches

class MultiHeadAttentionLSA(tf.keras.layers.MultiHeadAttention):
    def __init__(
        self,
        tau=None, #modificato, prima non c'era
        **kwargs
    ):
        super(MultiHeadAttentionLSA,self).__init__(**kwargs)
        self.tau = tf.Variable(math.sqrt(float(self._key_dim)), trainable=True) # The trainable temperature term. The initial value is the square root of the key dimension.

    def get_config(self):
      config = super().get_config().copy()
      config.update({
          "tau": self.tau.numpy(), #modificato, prima era solo self.tau
      })
      return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)

    def _compute_attention(self, query, key, value, attention_mask=None, training=None):
        query = tf.multiply(query, 1.0 / self.tau)
        attention_scores = tf.einsum(self._dot_product_equation, key, query)
        attention_scores = self._masked_softmax(attention_scores, attention_mask) 
        attention_scores_dropout = self._dropout_layer(
            attention_scores, training=training
        )
        attention_output = tf.einsum(
            self._combine_equation, attention_scores_dropout, value
        )
        return attention_output, attention_scores

def mlp(x, hidden_units, dropout_rate):
    for units in hidden_units:
        x = layers.Dense(units, activation=tf.nn.gelu)(x) 
        x = layers.Dropout(dropout_rate)(x)
    return x

diag_attn_mask = 1 - tf.eye(NUM_PATCHES)
diag_attn_mask = tf.cast([diag_attn_mask], dtype=tf.int8)