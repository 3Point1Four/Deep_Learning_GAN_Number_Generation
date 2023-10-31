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

# Apply a logarithmic transformation to x-values
data['Sample Number (log)'] = np.log1p(data['Sample Number'])

# Create a separate graph for each unique iteration value
unique_iterations = data['Iteration'].unique()

# Set plot parameters
sns.set(style="darkgrid")

for iteration in unique_iterations:
    plt.figure(figsize=(12, 6))
    subset = data[data['Iteration'] == iteration]
    sns.lineplot(data=subset, x="Sample Number (log)", y="Discriminator Value", label="Discriminator", linewidth=0.5)
    sns.lineplot(data=subset, x="Sample Number (log)", y="Generator Value", label="Generator", linewidth=0.5)
    
    # Configure x-axis notches
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.2f}"))
    
    # Add a prominent legend
    plt.legend(title="Legend")

    # Add labels and title
    plt.title(f"Iteration {iteration}")
    plt.xlabel("Log(Sample Number)")
    plt.ylabel("Value")

    # Show the plot
    plt.show()
