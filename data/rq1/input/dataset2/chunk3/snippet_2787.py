#Source: https://stackoverflow.com/questions/60923917/apache-arrow-with-tensorflow-type-error-arrow-type-mismatch-expected-dtype-2
from functools import partial
import tensorflow as tf
import pyarrow.csv
import pyarrow as pa
from sklearn.preprocessing import Normalizer
import tensorflow_io.arrow as arrow_io
import pandas as pd

"""run arrow_mnist local"""

# total columns num of mnist
COLUMNS_LEN = 785
# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '5'

# set gpu config
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# from tensorflow demo
def model_fit(ds):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 1, activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  optimizer=tf.keras.optimizers.Adam(),
                  metrics=['accuracy'])

    model.fit(ds, epochs=10)
    return model


def read_and_process(filename):
    """Read the given CSV file and yield processed Arrow batches."""

    # Read a CSV file into an Arrow Table
    opts = pyarrow.csv.ReadOptions(use_threads=True, autogenerate_column_names=True)
    table = pyarrow.csv.read_csv(filename, opts)
    # Fit the feature transform
    df = table.to_pandas()

    # normalizer the value except 'target'
    # for preprocess
    mylist = []
    for i in range(COLUMNS_LEN - 1):
        tmp1 = 'f' + str(i+1)
        mylist.append(tmp1)

    scaler = Normalizer().fit(df[mylist])
    # Iterate over batches in the pyarrow.Table and apply processing
    for batch in table.to_batches():
        df = batch.to_pandas()

        # Process the batch and apply feature transform
        X_scaled = scaler.transform(df[mylist])

        my_dict = {'f0': df['f0']}
        for i in range(COLUMNS_LEN - 1):
            tmp2 = 'f' + str(i+1)
            my_dict[tmp2] = X_scaled[:, i]

        # use my_dict will be successful
        # df_scaled = pd.DataFrame(my_dict)
        df_scaled = pd.DataFrame(df)

        batch_scaled = pa.RecordBatch.from_pandas(df_scaled, preserve_index=False)

        yield batch_scaled


def make_local_dataset(filename):
    """Make a TensorFlow Arrow Dataset that reads from a local CSV file."""

    # Read the local file and get a record batch iterator
    batch_iter = read_and_process(filename)

    # make output_types
    my_types_list = [tf.int64]
    for i in range(COLUMNS_LEN - 1):
        my_types_list.append(tf.float64)
    my_types_tuple = tuple(my_types_list)

    # make output_shapes
    my_shapes_list = []
    for i in range(COLUMNS_LEN):
        my_shapes_list.append(tf.TensorShape([]))
    my_shapes_tuple = tuple(my_shapes_list)

    # Create the Arrow Dataset as a stream from local iterator of record batches
    ds = arrow_io.ArrowStreamDataset.from_record_batches(
        batch_iter,
        batch_size=500,
        batch_mode='keep_remainder',
        output_types=my_types_tuple,
        output_shapes=my_shapes_tuple,
        record_batch_iter_factory=partial(read_and_process, filename))

    def my_map_func(*args):
        data_list = []
        # split the label and data
        flag = 1
        for i in args:
            if flag == 1:
                data_label = i
                flag = flag + 1
            else:
                data_list.append(i)

        data_tensor = tf.stack(data_list, axis=1)

        # reshape data to (28, 28 , 1)
        data_tensor_reshape = tf.reshape(data_tensor, (-1, 28, 28, 1))

        # return with label
        return (data_tensor_reshape, data_label)

    ds = ds.map(my_map_func)
    return ds


if __name__ == '__main__':

    ds = make_local_dataset('/home/maqy/data/mnist_test.csv')

    print("hello")
    model = model_fit(ds)