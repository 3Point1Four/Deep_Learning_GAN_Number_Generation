import numpy as np
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

def clean_mnist_data(x, y):
    clean_indices = []
    for i in range(len(x)):
        image = x[i]
        label = y[i]
        if image.min() == 0 and image.max() == 0:
            continue
        if (label < 0) or (label > 9):
            continue
        clean_indices.append(i)
    x_clean = x[clean_indices]
    y_clean = y[clean_indices]

    return x_clean, y_clean

x_train_clean, y_train_clean = clean_mnist_data(x_train, y_train)

x_test_clean, y_test_clean = clean_mnist_data(x_test, y_test)

removed_samples = len(x_train) - len(x_train_clean)
print(f"Removed {removed_samples} samples from the training data.")
removed_samples = len(x_test) - len(x_test_clean)
print(f"Removed {removed_samples} samples from the test data.")

print("Training data shape:", x_train_clean.shape, y_train_clean.shape)
print("Test data shape:", x_test_clean.shape, y_test_clean.shape)