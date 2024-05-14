#Source: https://stackoverflow.com/questions/63164902/getting-typeerror-expected-int32-got-none-of-type-nonetype-instead
class encoder_decoder(tf.keras.Model):
  def __init__(self,embedding_size,encoder_inputs_length,output_length,vocab_size,output_vocab_size,score_fun,units):
    super(encoder_decoder,self).__init__()
    self.vocab_size = vocab_size
    self.enc_units = units
    self.embedding_size = embedding_size
    self.encoder_inputs_length = encoder_inputs_length
    self.output_length = output_length
    self.lstm_output = 0
    self.state_h = 0
    self.state_c = 0
    self.output_vocab_size = output_vocab_size
    self.dec_units = units
    self.score_fun = score_fun
    self.att_units = units
    self.encoder=Encoder(self.vocab_size,self.embedding_size,self.enc_units,self.encoder_inputs_length)
    self.decoder = Decoder(self.output_vocab_size, self.embedding_size, self.output_length, self.dec_units ,self.score_fun ,self.att_units)
    # self.dense = Dense(self.output_vocab_size,activation = "softmax")
  
  def call(self,data):
    input,output = data[0],data[1]
    encoder_hidden = self.encoder.initialize_states(input.shape[0])
    encoder_output,encoder_hidden,encoder_cell = self.encoder(input,encoder_hidden)
    decoder_hidden = encoder_hidden
    decoder_cell =encoder_cell
    decoder_output = self.decoder(output,encoder_output,decoder_hidden,decoder_cell)
    return decoder_output