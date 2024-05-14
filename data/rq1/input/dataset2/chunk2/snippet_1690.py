#Source: https://stackoverflow.com/questions/56377141/typeerror-f1-score-got-an-unexpected-keyword-argument-average
Y_dev_pred = self.model.predict([self.dev[0], self.dev[1]], batch_size=self.BatchSize, verbose=0)
Y_dev_pred = np.argmax(Y_dev_pred, axis=1)
self.Y_dev = np.argmax(self.dev[2], axis=1)
print('####### ', self.Y_dev.shape, ' ', Y_dev_pred.shape)
print(self.Y_dev, ' ### ', Y_dev_pred)
print(f1_score(self.Y_dev, Y_dev_pred, average='macro'))