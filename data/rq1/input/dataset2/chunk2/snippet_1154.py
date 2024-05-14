#Source: https://stackoverflow.com/questions/64654126/numpy-typeerror-must-be-integer-not-tuple
import numpy as np
import matplotlib.pyplot as plt


def load_data(path):
    datum= []
    with open(path) as fp:
        line = fp.readline()
        while line:
            arr_line= line.split(",")
            datum.append(arr_line)
            line=fp.readline()
    return datum

#Sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))

#Loss function
def square_loss(y_pred, target):
    return np.mean(pow(((y_pred - target),2)))

if __name__ == "__main__":
    # load the data from the file
    matrix_data = load_data("all_data.txt")
    np.array(matrix_data)

    np.random.shuffle(matrix_data)

    training_data = matrix_data[167:,:] #These all lines gives error
    test_data = matrix_data[41:,:] #These all lines gives error

    X_tr, y_tr = training_data[:, :-1], training_data[:, -1] #These all lines gives error
    X_te, y_te = test_data[:, :-1], test_data[:, -1] #These all lines gives error
 
    