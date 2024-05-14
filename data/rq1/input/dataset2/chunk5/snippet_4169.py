#Source: https://stackoverflow.com/questions/62937599/in-accessing-intermediate-layers-of-keras-pretrained-model-error-message-att
class Network(base_layer.Layer):
  """A `Network` is a composition of layers.

  `Network` is the topological form of a "model". A `Model`
  is simply a `Network` with added training routines.

  Two types of `Networks` exist: Graph Networks and Subclass Networks. Graph
  networks are used in the Keras Functional and Sequential APIs. Subclassed
  networks are used when a user subclasses the `Model` class. In general,
  more Keras features are supported with Graph Networks than with Subclassed
  Networks, specifically:

  - Model cloning (`keras.models.clone`)
  - Serialization (`model.get_config()/from_config`, `model.to_json()/to_yaml()`
  - Whole-model saving (`model.save()`)

  A Graph Network can be instantiated by passing two arguments to `__init__`.
  The first argument is the `keras.Input` Tensors that represent the inputs
  to the Network. The second argument specifies the output Tensors that
  represent the outputs of this Network. Both arguments can be a nested
  structure of Tensors.

  Example:

  ```
  inputs = {'x1': keras.Input(shape=(10,)), 'x2': keras.Input(shape=(1,))}
  t = keras.layers.Dense(1, activation='relu')(inputs['x1'])
  outputs = keras.layers.Add()([t, inputs['x2'])
  network = Network(inputs, outputs)
  ```

  A Graph Network constructed using the Functional API can also include raw
  TensorFlow functions, with the exception of functions that create Variables
  or assign ops.

  Example:

  ```
  inputs = keras.Input(shape=(10,))
  x = keras.layers.Dense(1)(inputs)
  outputs = tf.nn.relu(x)
  network = Network(inputs, outputs)
  ```

  Subclassed Networks can be instantiated via `name` and (optional) `dynamic`
  keyword arguments. Subclassed Networks keep track of their Layers, and their
  `call` method can be overridden. Subclassed Networks are typically created
  indirectly, by subclassing the `Model` class.

  Example:

  ```
  class MyModel(keras.Model):
    def __init__(self):
      super(MyModel, self).__init__(name='my_model', dynamic=False)

      self.layer1 = keras.layers.Dense(10, activation='relu')

    def call(self, inputs):
      return self.layer1(inputs)
  ```

  Allowed args in `super().__init__`:
    name: String name of the model.
    dynamic: (Subclassed models only) Set this to `True` if your model should
      only be run eagerly, and should not be used to generate a static
      computation graph. This attribute is automatically set for Functional API
      models.
    trainable: Boolean, whether the model's variables should be trainable.
    dtype: (Subclassed models only) Default dtype of the model's weights (
      default of `None` means use the type of the first input). This attribute
      has no effect on Functional API models, which do not have weights of their
      own.
  """

  # See tf.Module for the usage of this property.
  # The key of _layer_call_argspecs is a layer. tf.Module._flatten will fail to
  # flatten the key since it is trying to convert Trackable/Layer to a string.
  _TF_MODULE_IGNORED_PROPERTIES = frozenset(itertools.chain(
      ('_layer_call_argspecs', '_compiled_trainable_state'),
      base_layer.Layer._TF_MODULE_IGNORED_PROPERTIES
  ))