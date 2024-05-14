#Source: https://stackoverflow.com/questions/58584845/typeerror-float-object-is-not-subscriptable-python
import numpy as np
import matplotlib.pyplot as plt


class Implementation:
    def __init__(self):
        pass

    def Distancess(self, training_sub_data, query_instance):

        query_params = query_instance[:10]

        eucl = np.sqrt(np.sum((training_sub_data - query_params) ** 2, axis=-1))
        return eucl, np.argsort(eucl)

    def weight(self, training_data, distances, sorted_indices, k):
        i = 1
        samples_class = training_data[sorted_indices[:k]][:, -1]
        nearest_distances = distances[sorted_indices[:k]]
        nearest_weights = np.divide(1, np.square(nearest_distances))
        class_0_weights_sum = np.sum(nearest_weights[samples_class == 0])
        class_1_weights_sum = np.sum(nearest_weights[samples_class == 1])
        class_2_weights_sum = np.sum(nearest_weights[samples_class == 2])

        if class_0_weights_sum > class_1_weights_sum and class_0_weights_sum > class_2_weights_sum:
            return 0
        elif class_1_weights_sum > class_0_weights_sum and class_1_weights_sum > class_2_weights_sum:
            return 1
        else:
            return 2

def weight_based_approach(training_data, test_data, kn_k_value):
    training_data_10_columns = training_data[:, :10]

    kn = Implementation()

    eucl_weight_prediction_count = 0
    for query_instance in test_data:
        distances, euclidean_indices = kn.Distancess(training_data_10_columns, query_instance)

        weight_based_average = kn.weight(training_data, distances, euclidean_indices, kn_k_value)

        if query_instance[-1] == weight_based_average:
            eucl_weight_prediction_count += 1

    return eucl_weight_prediction_count / len(test_data) * 100


def main():
    global accuracies
    euclidean_accuracies = []
    k_samples = []
    k_samples.extend(list(range(1, 4, 1)))

    print("Range" + str(k_samples))

    for k in k_samples:
        training_file = "classification/trainingData.csv"
        test_file = "classification/testData.csv"
        kn_k_value = k

        training_data = np.genfromtxt(training_file, delimiter=",")
        test_data = np.genfromtxt(test_file, delimiter=",")

        accuracies = weight_based_approach(training_data, test_data, kn_k_value)
        euclidean_accuracies.append(accuracies[0])

    print("distance: " + str(euclidean_accuracies))

    plt.plot(k_samples, euclidean_accuracies, 'r')
    plt.xlabel('K{Number of Nearest Neighbour(s)}')
    plt.ylabel('Accuracy %')
    plt.title('K vs Accuracy graph')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()