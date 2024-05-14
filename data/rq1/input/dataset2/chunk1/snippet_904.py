#Source: https://stackoverflow.com/questions/64665776/typeerror-cant-pickle-weakref-objects-when-pickling-a-deep-learning-model
model = Sequential()

model.add( Dense(30,activation='relu') )
model.add( Dropout(0.5) ) 
model.add( Dense(20,activation='relu') )
model.add( Dropout(0.5) ) 
model.add( Dense(20,activation='relu') )
model.add( Dropout(0.5) )     
model.add( Dense(1,activation='sigmoid') )

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy']) 