#Source: https://stackoverflow.com/questions/55559561/nameerror-name-model-is-not-defined-in-python-code-for-isolated-speech-recogn
from sklearn.model_selection import StratifiedShuffleSplit
sss = StratifiedShuffleSplit(test_size=0.1, random_state=0)

for n,i in enumerate(all_obs):
    all_obs[n] /= all_obs[n].sum(axis=0)


for train_index, test_index in sss.split(all_obs, all_labels):
    X_train, X_test = all_obs[train_index, ...], all_obs[test_index, ...]
    y_train, y_test = all_labels[train_index], all_labels[test_index]
ys = set(all_labels)
ms = [gmmhmm(7) for y in ys]

_ = [model.train(X_train[y_train == y, :, :]) for m, y in zip(ms, ys)]
ps1 = [model.test(X_test) for m in ms]
res1 = np.vstack(ps1)
predicted_label1 = np.argmax(res1, axis=0)
dictionary = ['apple', 'banana', 'elephant', 'dog', 'frog', 'cat', 'jack', 'god', 'Intelligent', 'hello']
spoken_word = []
for i in predicted_label1:
    spoken_word.append(dictionary[i])
print(spoken_word)
missed = (predicted_label1 != y_test)
print('Test accuracy: %.2f percent' % (100 * (1 - np.mean(missed))))