#Source: https://stackoverflow.com/questions/61808747/filenotfounderror-winerror-3-when-using-two-concatenated-strings
DIR = r"D:/My/Directory"
classes = ['itemA', 'itemB']


for item in classes:
    for scope in ["training/", "testing/"]:
        os.mkdir(os.path.join(DIR, scope + item))