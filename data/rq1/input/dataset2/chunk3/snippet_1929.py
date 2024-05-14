#Source: https://stackoverflow.com/questions/77260287/typeerror-cant-convert-cuda0-device-type-tensor-to-numpy-use-tensor-cpu-to
plt.plot(train_accuracy, label='training accuracy')
plt.plot(test_accuracy, label='validation accuracy')
plt.title('Accuracy at the end of each epoch')
plt.legend();