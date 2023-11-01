import numpy as np
from tensorflow import keras
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train, y_train), (_, _) = mnist.load_data()

label_counts = np.bincount(y_train)

thresholds = [0.0, 0.1, 0.2, 0.4, 0.8, 1.0]

normalized_data = [np.copy(x_train) for _ in range(len(thresholds))]

for t_index, threshold in enumerate(thresholds):
    for label in range(10):
        label_indices = np.where(y_train == label)[0]
        for i in range(min(5, label_counts[label])):
            index = label_indices[i]
            original_image = x_train[index].astype(float) / 255.0

num_columns = len(thresholds)
fig, axes = plt.subplots(10, num_columns, figsize=(15, 25))

for t_index, threshold in enumerate(thresholds):
    for label in range(10):
        label_indices = np.where(y_train == label)[0]
        for i in range(5):
            index = label_indices[i]
            original_image = x_train[index]
            normalized_image = (normalized_data[t_index][index] * 255).astype(int)
            difference = differences[t_index][index]

            ax = axes[label, t_index]
            ax.imshow(np.hstack((original_image, normalized_image)), cmap='gray', aspect='auto')
            ax.set_title(f"Thresh: {threshold:.3f}\nLabel: {label}, Img: {i + 1}\nDiff: {np.max(difference)}",
                         fontsize=8)
            ax.axis('off')

plt.tight_layout()
plt.subplots_adjust(wspace=0.1, hspace=0.2)
plt.show()
