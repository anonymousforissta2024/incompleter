#Source: https://stackoverflow.com/questions/41297838/using-python-3-5-throwing-error-typeerror-a-bytes-like-object-is-required-no
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))