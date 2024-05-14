#Source: https://stackoverflow.com/questions/59274292/type-error-when-trying-to-list-all-the-sub-directories-of-a-directory
TRAIN_PATH_ARRAY=['New folder/train/']
TEST_PATH_ARRAY=['New folder/test/']
train_ids = next(os.walk(TRAIN_PATH_ARRAY))[1]
test_ids = next(os.walk(TEST_PATH_ARRAY))[1]
np.random.seed(10)