#Source: https://stackoverflow.com/questions/60296710/attributeerror-dataset-object-has-no-attribute-c-fastai
X = list(df['input_img'])
y = list(df['mask_img'])

X_train, X_valid, y_train, y_valid = train_test_split(
     X, y, test_size=0.33, random_state=42)

class NumbersDataset():
    def __init__(self, inputs, labels):
        self.X = inputs
        self.y = labels

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        img_train = cv2.imread(self.X[idx])
        img_mask = cv2.imread(self.y[idx])
        img_train = cv2.resize(img_train, (427,240), interpolation = cv2.INTER_LANCZOS4) 
        img_mask = cv2.resize(img_mask, (427,240), interpolation = cv2.INTER_LANCZOS4) 
        return img_train, img_mask