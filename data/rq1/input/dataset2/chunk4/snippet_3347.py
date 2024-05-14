#Source: https://stackoverflow.com/questions/77544820/attributeerror-tensorflow-python-util-pywrap-checkpoint-reader-c-object-has
# Directory where the checkpoints will be saved
checkpoint_dir = "./training_checkpoints"
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True
)

checkpoint_num = 10
model.load_weights(tf.train.load_checkpoint('./training_checkpoints/ckpt_' + str(checkpoint_num)))
model.build(tf.TensorShape([1, None]))