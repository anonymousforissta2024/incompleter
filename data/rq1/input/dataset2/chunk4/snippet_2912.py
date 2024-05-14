#Source: https://stackoverflow.com/questions/67485998/estimator-predict-typeerror-expected-any-non-tensor-type-got-a-tensor-instea
# Create the classifier
print("Creating classifier from {}".format(checkpoint_path))
classifier = tf.estimator.Estimator(
    model_fn=vgg_model_fn,
    params=params,
    model_dir=checkpoint_path,
)

print("Computing predictions")
predictions = classifier.predict(
    input_fn=tf.estimator.inputs.numpy_input_fn(
        {"x": video},
        batch_size=1,
        shuffle=False,
    )
)

# Print predictions
predictions = list(predictions)
predicted_class = predictions["classes"]
top_k_classes = (-predictions["probabilities"]).argsort()[:int(k)]