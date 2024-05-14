#Source: https://stackoverflow.com/questions/69720033/typeerror-not-supported-between-instances-of-int-and-str-when-i-run-t
from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(df['Base_Reviews'], df['My_Labels'],
                                                    stratify=df['My_Labels'], 
                                                    test_size=0.25)
print("Train shape : ",train_X.shape)
print("Test shape : ",test_X.shape)
## Tokenize the sentences
tokenizer = Tokenizer(num_words= max_features)
tokenizer.fit_on_texts(list(train_X))
train_X = tokenizer.texts_to_sequences(train_X)
test_X = tokenizer.texts_to_sequences(test_X)

## Pad the sentences 
train_X = pad_sequences(train_X, maxlen=maxlen)
test_X = pad_sequences(test_X, maxlen=maxlen)