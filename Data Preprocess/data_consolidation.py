import tensorflow as tf
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

train_shape = x_train.shape
test_shape = x_test.shape

num_train_samples = train_shape[0]
num_test_samples = test_shape[0]

num_train_values = train_shape[1] * train_shape[2]
num_test_values = test_shape[1] * test_shape[2]

print("Training Data:")
print(f"Shape: {train_shape}")
print(f"Number of Samples: {num_train_samples}")
print(f"Number of Values in Each Column (Image Dimensions): {num_train_values}")

print("\nTesting Data:")
print(f"Shape: {test_shape}")
print(f"Number of Samples: {num_test_samples}")
print(f"Number of Values in Each Column (Image Dimensions): {num_test_values}")