#Source: https://stackoverflow.com/questions/70546376/any-way-to-fix-this-typeerror-a-bytes-like-object-is-required-not-str-when-o
with open("final_project_dataset.pkl", "rb") as data_file:
        data_dict = pickle.load(data_file, encoding='utf8')