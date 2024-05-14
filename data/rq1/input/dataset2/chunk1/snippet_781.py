#Source: https://stackoverflow.com/questions/50997928/typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index-with-1d
bin_probs = [0.5, 0.3, 0.15, 0.04, 0.0025, 0.0025, 0.001, 0.001, 0.001, 0.001, 0.001]

X_train = list(range(2000000))

train_probs = bin_probs * int(len(X_train) / len(bin_probs)) # extend probabilities across bin elements
train_probs.extend([0.001]*(len(X_train) - len(train_probs))) # a small fix to match number of elements
train_probs = train_probs/np.sum(train_probs) # normalize
indices = np.random.choice(range(len(X_train)), replace=False, size=50000, p=train_probs)
out_images = X_train[indices.astype(int)] # this is where I get the error