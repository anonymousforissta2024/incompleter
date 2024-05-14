#Source: https://stackoverflow.com/questions/76790765/typeerror-exception-encountered-when-calling-layer-convtokenizer-type-convto
# Compile
opt = AdamW(learning_rate=Learning_Rate, weight_decay=Weight_Decay)
model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=opt,
    metrics=[
        Accuracy(name="Top1Accuracy"), TopKAccuracy(k=3, name="Top3Accuracy")
    ]
)

history = model.fit(
    train_ds,
    validation_data=test_ds, 
    epochs=5
)