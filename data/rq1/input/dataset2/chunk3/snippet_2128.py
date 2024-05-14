#Source: https://stackoverflow.com/questions/69620035/typeerror-dimension-value-must-be-integer-or-none-in-keras-vq-vae-example
# Create a mini sampler model.
inputs = layers.Input(shape=pixel_cnn.input_shape[1:])
x = pixel_cnn(inputs, training=False)
dist = tfp.distributions.Categorical(logits=x)
sampled = dist.sample()
sampler = keras.Model(inputs, sampled)

# Create an empty array of priors.
batch = 10
priors = np.zeros(shape=(batch,) + (pixel_cnn.input_shape)[1:])
batch, rows, cols = priors.shape

# Iterate over the priors because generation has to be done sequentially pixel by pixel.
for row in range(rows):
    for col in range(cols):
        # Feed the whole array and retrieving the pixel value probabilities for the next
        # pixel.
        probs = sampler.predict(priors)
        # Use the probabilities to pick pixel values and append the values to the priors.
        priors[:, row, col] = probs[:, row, col]

print(f"Prior shape: {priors.shape}")