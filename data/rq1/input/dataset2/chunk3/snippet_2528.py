#Source: https://stackoverflow.com/questions/64055916/typeerror-with-dense-block-of-densenet-in-tensorflow-2
class DenseBlock(Layer):

  def __init__(self, nb_layers, nb_filter, growth_rate, dropout_rate=None, grow_nb_filters=True, **kwargs):

    super(DenseBlock, self).__init__(**kwargs)
    self.nb_layers = nb_layers
    self.growth_rate =growth_rate
    self.nb_filter = nb_filter
    self.grow_nb_filters = grow_nb_filters
    self.conv_blocks = [ConvBlock(growth_rate, dropout_rate) for i in range(nb_layers)]

  def call(self, inputs):
    concat_feat = tf.cast(inputs, dtype=tf.float32)
    for conv in self.conv_blocks:

        x = conv
        concat_feat = tf.concat([concat_feat, x], -1)

        if self.grow_nb_filters:
            self.nb_filter += self.growth_rate

    return concat_feat, self.nb_filter