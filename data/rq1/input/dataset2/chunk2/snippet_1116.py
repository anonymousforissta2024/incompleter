#Source: https://stackoverflow.com/questions/69209908/tensorflow-typeerror-generator-object-is-not-callable
converter.representative_dataset = my_batch_generator(data)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
converter._experimental_lower_tensor_list_ops = False
quantized_tflite_model = converter.convert()