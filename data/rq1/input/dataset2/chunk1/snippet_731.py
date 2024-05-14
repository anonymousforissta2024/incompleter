#Source: https://stackoverflow.com/questions/55884002/how-to-fix-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-i
labels = []
label_np = np.array(labels)

with open(path, encoding='utf-8') as in_file:
    data = csv.reader(in_file)
    for line in data:
        label_ = np.append(label_np, line)

model = SVC(kernel='linear')
total_svm = []
total_mat_svm = np.zeros((2,2))

kf = StratifiedKFold(n_splits=3)
kf.get_n_splits(result_preprocess, label_)

for train_index, test_index in kf.split(result_preprocess, label_):
    # print('Train : ', test_index, 'Test : ', test_index)
    x_train, x_test = result_preprocess[train_index], result_preprocess[test_index]
    y_train, y_test = label_[train_index], label_[test_index]

vectorizer = TfidfVectorizer(min_df=5,
                             max_df=0.8,
                             sublinear_tf=True,
                             use_idf=True)
train_vector = vectorizer.fit_transform(x_train)
test_vector = vectorizer.transform(x_test)

model.fit(x_train, y_train)
hasil_svm = model.predict(x_test)

total_mat_svm = total_mat_svm + confusion_matrix(y_test, hasil_svm)
total_svm = total_mat_svm + sum(y_test==hasil_svm)

print(total_mat_svm)