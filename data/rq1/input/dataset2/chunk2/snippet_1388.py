#Source: https://stackoverflow.com/questions/68429511/attributeerror-list-object-has-no-attribute-reshape-when-using-reshape-for
w_train, w_test, y_train, y_test =train_test_split(w, y, test_size=0.2 ,shuffle=True, random_state=42)

w_train = w_train.reshape(2404,28,224,224,3)
w_test = w_test.reshape(601,28,224,224,3)