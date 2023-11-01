
<h1 align="center">Deep Learning Number Generation</h1>

  

<h2 align="center">Overview</h2>

<p align="center">This repository contains code for training a Generative Adversarial Network (GAN) to generate images of handwritten digits. The generated images can be customized to correspond to a specified digit. Below are instructions on how to run the code and check the examples.</p>

  > [skip to view without running](#skip)<```click here```

<h2 align="center">Pre Requisites</h2>

To run the code in this repository, make sure you have the following installed:

  

- Python (>= 11.5)

- Jupyter Notebook

  

<p align="center"><strong>Before running the code, you'll need to install the necessary libraries. You can do this using pip:</strong></p>

  

```bash

pip  install  keras

```

  

```bash

pip  install  matplotlib

```

  

```bash

pip  install  tensorflow

```

  

```bash

pip  install  numpy

```

  

```bash

pip  install  seaborn

```

  

```bash

pip  install  pandas

```

  

```bash

pip  install  sklearn

```

  

```bash

pip  install  Pillow

```

  

```bash

pip  install  svgwrite

```

  

```bash

pip  install  regex

```

  

```bash

pip  install  Ipython

```

  

<h2 align="center">  <strong>Running the Code</strong></h2>

  

<h1 align="center"> 1. Running the model (GAN_INIT.ipynb)</h1>

### 1.1 Open the Jupyter Notebook.

### 1.2 Navigate to the GAN_INIT notebook.

### 1.3 Run GAN_INIT. Please note that GAN_INIT may take approximately 30 minutes to run, but the runtime may vary depending on your hardware.

  

<h1 align="center">OR<h1>

  

<h1 align="center">1. Running the model (GAN_SECOND_RUN.ipynb)<h1>

### 1.1 Open the Jupyter Notebook.

### 1.2 Navigate to the GAN_SECOND_RUN notebook.

### 1.3 Run GAN_SECOND_RUN. This notebook contains two runs:

- The first run may take several hours to train, and the runtime may vary based on your hardware.

- The second run typically takes approximately 2 hours, but the runtime may vary based on your hardware.

  

<h1 align="center"> 2.  Checking the Examples</h1>

  

### 2.1 Input a Specified Digit

- After training the model, you can input a specified digit value.

###  2.2 DFS Code (DFS.ipynb)

- Run the DFS code.

- The code will generate output.

### 2.3 svg_lines_curves_OP

- Run the svg_lines_curves_OP code.

-  The final output will be saved as SVG files.

  

> Please note that running times may vary depending on your hardware. If you encounter any issues or have questions, feel free to reach out for assistance.

### <a id="skip"></a><p align="center">Viewing Output without running</p>

There are 2 folders containing outputs. 

## Running_Assets

### This folder contains assets used when running the code the first time.

#### Important files are:
- 9.png 
![9.png](https://github.com/3Point1Four/Deep_Learning_GAN_Number_Generation/blob/main/Running_Assets/9.png)
This is the example image requested after GAN was run first.
- skeleton_image.png
![skeleton image](https://github.com/3Point1Four/Deep_Learning_GAN_Number_Generation/blob/main/Running_Assets/skeleton_image.png)
This is the image skeleton of said example.

- final_path.txt
This is a text file containing the points extrapolated.

## OP_Assets

### This folder contains assets as the final output.

#### Important files are:

- output_lines.svg
![blocky figure 9](https://github.com/3Point1Four/Deep_Learning_GAN_Number_Generation/blob/main/OP_Assets/output_lines%20.svg)
Final vector output without any curvature applied.

- output_curves.svg
![smoother figure 9](https://github.com/3Point1Four/Deep_Learning_GAN_Number_Generation/blob/main/OP_Assets/output_curves.svg)
Final vector output with curvature applied.


Happy digit generation!
