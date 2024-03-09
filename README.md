# Color Picker and Highlighter Documentation

This project encompasses a Python script designed to facilitate the selection of a specific color from a given image, and to subsequently highlight regions within that image which closely match the chosen color, adjustable by a user-defined threshold. This document aims to delineate the procedure required to effectively operate the script.

## Prerequisites

Before running the script, ensure you have Python installed on your system along with the necessary Python libraries. You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```



## Installation

### Clone the Repository

Initiate by cloning this repository to your local device utilizing Git. Execute the ensuing command within a terminal interface:

```bash
git clone https://github.com/ADA-GWU/a2-digital-image-and-color-spaces-tmehtiyev2019.git
```

### Navigate to the Project Directory

Transition into the project directory with the command:

```bash
cd a2-digital-image-and-color-spaces-tmehtiyev2019
```



## Running the Script

To operationalize the script, an image file must be situated within the project directory or be accessible through a specified path. The script accepts two parameters:

- `image_path`: The path directing to the image file.
- `--threshold` (optional): The threshold for color similarity, defaulting to 50 if unspecified.

Employ the following command to execute the script:

```bash
python main.py <image_path> --threshold <value>
```


Replace `<image_path>` with the path to your image file, and `<value>` with the preferred threshold value for color similarity. For instance:


```bash
python main.py photos/matryoshka.jpeg --threshold 50
```

## Usage Example

Upon executing the script with the command specified above, a window will be displayed showcasing the chosen image. Clicking any region of the image will select a color, post which, the script will highlight areas within the image that are of a color similar to the one selected.




