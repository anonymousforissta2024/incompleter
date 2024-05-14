#Source: https://stackoverflow.com/questions/43403426/training-doc2vec-on-20newsgroups-dataset-getting-exception-attributeerror-str
model.train(train_docs, total_examples = len(train_docs), epochs = model.iter)
model.train_words = False
model.train_labels = True
model.train(test_docs, total_examples = len(test_docs), epochs = model.iter)

model.save(output)