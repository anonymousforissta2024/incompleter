#Source: https://stackoverflow.com/questions/71143690/typeerror-expected-int32-passed-to-parameter-size-of-op-slice-got-4608-0
def ourmodel(numberOfLSTMcells=3,n_timesteps_in=3000,n_features=61):

    inp =Input(shape=(n_timesteps_in, n_features))
    lstm= LSTM(numberOfLSTMcells,return_sequences=True, return_state=False) (inp)
    flatten=Flatten()(lstm)
    fc=Dense(64,activation='relu')(flatten)
    fc=Dense(32,activation='relu')(fc)
    out=Dense(1,activation='sigmoid')(fc)

    model = Model(inputs=inp, outputs=out)
    model.compile(loss='binary_crossentropy', optimizer='adam', 
                  metrics=['accuracy'])
    return model

model=ourmodel()
model.fit(data_array,y=label_array,batch_size=1024*0.1,epochs=50,verbose=0)