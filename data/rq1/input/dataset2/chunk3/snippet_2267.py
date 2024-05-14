#Source: https://stackoverflow.com/questions/57979712/attributeerror-module-tensorflow-has-no-attribute-get-default-graph-i-am-g
ml = Sequential()
ml.add(LSTM(64,dropout=0.5, recurrent_dropout=0.5,return_sequences=True))