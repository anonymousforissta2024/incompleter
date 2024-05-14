#Source: https://stackoverflow.com/questions/49204913/tensorflow-use-tf-data-textlinedataset-return-attributeerror-list-object-ha
import tensorflow as tf
feature_names = ['length_1',
             'width_1',
             'length_2',
             'width_2']
FILE_TRAIN = 'iris_training.csv'
FILE_TEST = 'iris_test.csv'
def my_input_fn(file_path, perform_shuffle=False, repeat_count=1):
    def decode_csv(line):
        parsed_line = tf.decode_csv(line, [[0.], [0.], [0.], [0.], [0]])
        label = parsed_line[-1:]  # Last element is the label
        del parsed_line[-1]  # Delete last element
        features = parsed_line
        d = dict(zip(feature_names, features))
        return d, label

    dataset = tf.data.TextLineDataset(file_path).skip(1).map(decode_csv)  # Transform each elem by applying decode_csv fn
    if perform_shuffle:
        # Randomizes input using a window of 256 elements (read into memory)
        dataset = dataset.shuffle(buffer_size=256)
    dataset = dataset.repeat(repeat_count)  # Repeats dataset this # times
    dataset = dataset.batch(32)  # Batch size to use
    iterator = dataset.make_one_shot_iterator()
    batch_features, batch_labels = iterator.get_next()
    return batch_features, batch_labels
next_batch = my_input_fn(FILE_TRAIN, True)  # Will return 32 random elements
feature_columns = [tf.feature_column.numeric_column(k) for k in feature_names]
classifier = tf.estimator.DNNClassifier(
    feature_columns=feature_columns,  # The input features to our model
    hidden_units=[10, 10],  # Two layers, each with 10 neurons
    n_classes=3,
    model_dir='iris_model')  # Path to where checkpoints etc are stored
classifier.train(input_fn=lambda: my_input_fn(FILE_TRAIN, True, 8))
evaluate_result = classifier.evaluate(input_fn=lambda: my_input_fn(FILE_TEST, False, 4))
print("Evaluation results")

for key in evaluate_result:
    print("   {}, was: {}".format(key, evaluate_result[key]))