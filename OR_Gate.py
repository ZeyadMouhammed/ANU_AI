import numpy as np


# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)


# Input data for OR gate
# Inputs: [X1, X2] -> Outputs: [Y]
# X1, X2 = Inputs; Y = Output (1 if X1 or X2 is 1, else 0)
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [1]])

# Initialize weights and bias
np.random.seed(42)  # For reproducibility
weights = np.random.uniform(-1, 1, (2, 1))  # Random weights for 2 inputs
bias = np.random.uniform(-1, 1, (1,))  # Random bias

# Learning rate
learning_rate = 0.1

# Training the model
for epoch in range(10000):
    # Forward pass
    linear_output = np.dot(inputs, weights) + bias
    predictions = sigmoid(linear_output)

    # Calculate error
    error = outputs - predictions

    # Backpropagation (gradient descent step)
    d_predictions = error * sigmoid_derivative(predictions)  # Gradient of the error
    weights += np.dot(inputs.T, d_predictions) * learning_rate  # Update weights
    bias += np.sum(d_predictions) * learning_rate  # Update bias

# Testing the model after training
print("\nFinal Weights:", weights)
print("Final Bias:", bias)

print("\nPredictions:")
for i in range(len(inputs)):
    test_output = sigmoid(np.dot(inputs[i], weights) + bias)  # Test the inputs
    print(f"Input: {inputs[i]} => Predicted Output: {round(test_output[0])}")
