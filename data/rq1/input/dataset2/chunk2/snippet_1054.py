#Source: https://stackoverflow.com/questions/77469949/model-fit-typeerror-nonetype-object-is-not-callable
from tensorflow import keras
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

label_map = {label:num for num, label in enumerate(signs)}
label_map

sequences, labels = [], []
for sign in signs:
    for sequence in range(no_sequences):
        window = []
        for frame_no in range(sequence_length):
            res = np.load(os.path.join(Data_Path, sign, str(sequence),"{}.npy".format(frame_no)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[sign])

X = np.array(sequences)
X.shape

y = to_categorical(labels).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard

log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir = log_dir)


model = Sequential()
model.add(LSTM(64, return_sequences=True, activation="relu", input_shape=(30,1662)))
model.add(LSTM(128, return_sequences=True, activation="relu"))
model.add(LSTM(64, return_sequences=False, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(signs.shape[0], activation='softmax'))

model.compile(optimizer='Adam', loss="categorical_crossentropy", metrics=['categorical accuracy'])

model.fit(X_train, y_train, epochs=2000, callbacks=[tb_callback])