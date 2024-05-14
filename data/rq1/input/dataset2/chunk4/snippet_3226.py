#Source: https://stackoverflow.com/questions/75522713/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-when-trying-to
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from pyswarms.single.global_best import GlobalBestPSO

# Load the input and output data from a CSV file
# data = pd.read_csv('data.csv')

# Separate the input and output data

X=d3.iloc[:,:11]
y=d3.iloc[:,-1]


# Define the fitness function to optimize the SVR model
def svr_fitness_function(params):
    # Extract the SVR hyperparameters from the input vector
    C = params[0]
    gamma = params[1]
    epsilon = params[2]
    
    # Create a new SVR model with the given hyperparameters
    model = SVR(C=C, gamma=gamma.all(), epsilon=epsilon)
    
    # Train the model on the input and output data
    model.fit(X, y)
    
    # Use the trained model to make predictions on the input data
    y_pred = model.predict(X)
    
    # Calculate the mean squared error of the predictions
    mse = mean_squared_error(y, y_pred)
    
    # Return the negative of the mean squared error as the fitness value
    return -mse

# Set up the PSO optimizer
n_particles = 20
max_iter = 100
bounds = (np.array([0.1, 0.1, 0.1]), np.array([10, 10, 1]))
optimizer = GlobalBestPSO(n_particles=n_particles, dimensions=3, options={'c1': 0.5, 'c2': 0.3, 'w': 0.9})

# Run the PSO optimizer to find the optimal SVR hyperparameters
best_cost, best_params = optimizer.optimize(svr_fitness_function, iters=max_iter)

# Print the optimal SVR hyperparameters and the corresponding mean squared error
print('Optimal SVR hyperparameters:', best_params)
print('Corresponding mean squared error:', -best_cost)