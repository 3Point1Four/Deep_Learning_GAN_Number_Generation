import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Define regular expressions for extracting relevant information
regex_iteration = r'>(\d+), (\d+)/(\d+), d=([\d.]+), g=([\d.]+)'

# Create lists to store extracted information
iterations = []
sample_numbers = []
d_values = []
g_values = []

# Read the text file with the provided file path
file_path = r'C:\\Users\\Pirann\\Downloads\\GAN_run_2_OP.txt'

with open(file_path, 'r') as file:
    for line in file:
        match = re.search(regex_iteration, line)
        if match:
            iteration, sample_number, _, d_value, g_value = match.groups()
            iterations.append(int(iteration))
            sample_numbers.append(int(sample_number))
            d_values.append(float(d_value))
            g_values.append(float(g_value))

# Create a DataFrame to store the data
data = pd.DataFrame({
    'Iteration': iterations,
    'Sample Number': sample_numbers,
    'Discriminator Value': d_values,
    'Generator Value': g_values
})

# Apply Min-Max scaling to normalize the data
data['Sample Number (normalized)'] = (data['Sample Number'] - data['Sample Number'].min()) / (data['Sample Number'].max() - data['Sample Number'].min())
data['Discriminator Value (normalized)'] = (data['Discriminator Value'] - data['Discriminator Value'].min()) / (data['Discriminator Value'].max() - data['Discriminator Value'].min())

# Create a separate graph for each unique iteration value
unique_iterations = data['Iteration'].unique()

sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))

for iteration in unique_iterations:
    subset = data[data['Iteration'] == iteration]
    plt.figure()
    sns.lineplot(data=subset, x="Sample Number (normalized)", y="Discriminator Value (normalized)")
    plt.title(f"Iteration {iteration}")
    plt.xlabel("Normalized Sample Number")
    plt.ylabel("Normalized Discriminator Value")

plt.show()
