#Source: https://stackoverflow.com/questions/77284708/custom-peephole-lstm-layer-returns-typeerror
import tensorflow as tf

class PeepholeLSTM(tf.keras.layers.Layer):
    def __init__(self, units, activation='tanh', return_sequences=False, **kwargs):
        super(PeepholeLSTM, self).__init__(**kwargs)
        self.units = units
        self.activation = tf.keras.activations.get(activation)
        self.return_sequences = return_sequences

    def build(self, input_shape):
        input_dim = input_shape[-1]

        # Create weights for the LSTM cell
        self.Wf = self.add_weight(name='Wf', shape=(input_dim, self.units), initializer='glorot_uniform')
        self.Uf = self.add_weight(name='Uf', shape=(self.units, self.units), initializer='orthogonal')
        self.bf = self.add_weight(name='bf', shape=(self.units,), initializer='zeros')

        self.Wi = self.add_weight(name='Wi', shape=(input_dim, self.units), initializer='glorot_uniform')
        self.Ui = self.add_weight(name='Ui', shape=(self.units, self.units), initializer='orthogonal')
        self.bi = self.add_weight(name='bi', shape=(self.units,), initializer='zeros')

        self.Wc = self.add_weight(name='Wc', shape=(input_dim, self.units), initializer='glorot_uniform')
        self.Uc = self.add_weight(name='Uc', shape=(self.units, self.units), initializer='orthogonal')
        self.bc = self.add_weight(name='bc', shape=(self.units,), initializer='zeros')

        self.Wo = self.add_weight(name='Wo', shape=(input_dim, self.units), initializer='glorot_uniform')
        self.Uo = self.add_weight(name='Uo', shape=(self.units, self.units), initializer='orthogonal')
        self.bo = self.add_weight(name='bo', shape=(self.units,), initializer='zeros')

        self.c_peephole = self.add_weight(name='c_peephole', shape=(self.units,), initializer='zeros')
        self.o_peephole = self.add_weight(name='o_peephole', shape=(self.units,), initializer='zeros')

        self.built = True

    def call(self, inputs):
        # Initialize states
        batch_size, seq_length, _ = inputs.shape
        h_tm1 = tf.zeros(shape=(batch_size, self.units))
        c_tm1 = tf.zeros(shape=(batch_size, self.units))

        outputs = []

        for t in range(seq_length):
            x_t = inputs[:, t, :]
            f = tf.sigmoid(tf.matmul(x_t, self.Wf) + tf.matmul(h_tm1, self.Uf) + self.bf + self.c_peephole * c_tm1)
            i = tf.sigmoid(tf.matmul(x_t, self.Wi) + tf.matmul(h_tm1, self.Ui) + self.bi)
            c = f * c_tm1 + i * self.activation(tf.matmul(x_t, self.Wc) + tf.matmul(h_tm1, self.Uc) + self.bc)
            o = tf.sigmoid(tf.matmul(x_t, self.Wo) + tf.matmul(h_tm1, self.Uo) + self.bo + self.o_peephole * c)
            h = o * self.activation(c)

            outputs.append(h)
            h_tm1 = h
            c_tm1 = c

        if self.return_sequences:
            return tf.stack(outputs, axis=1)
        else:
            return h