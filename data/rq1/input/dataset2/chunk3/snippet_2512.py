#Source: https://stackoverflow.com/questions/67342655/multiclass-text-classification-typeerror-input-must-be-a-sparsetensor
# Split the data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.2, random_state=42)

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y_train)
encoded_y_train = encoder.transform(y_train)
# convert integers to dummy variables (i.e. one hot encoded)
y_train= np_utils.to_categorical(encoded_y_train)

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y_validation)
encoded_y_validation = encoder.transform(y_validation)
# convert integers to dummy variables (i.e. one hot encoded)
y_validation= np_utils.to_categorical(encoded_y_validation)

# The first document-term matrix has default Count Vectorizer values - counts of bigrams
from sklearn.feature_extraction.text import CountVectorizer

cv1 = CountVectorizer(analyzer='char',ngram_range=(2, 2))

X_train_cv1 = cv1.fit_transform(X_train)
X_validation_cv1  = cv1.transform(X_validation)

input_dim = X_train_cv1.shape[1]  # Number of features
model = Sequential()
model.add(layers.Dense(10, input_dim=input_dim, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

X_train_cv1 = tf.sparse.reorder(X_train_cv1)
y_train = tf.sparse.reorder(y_train)
X_validation_cv1 = tf.sparse.reorder(X_validation_cv1)
y_validation = tf.sparse.reorder(y_validation)

history = model.fit(X_train_cv1, y_train,epochs=100,verbose=True,validation_data=(X_validation_cv1, y_validation),batch_size=10)