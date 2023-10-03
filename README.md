# Image Conversion Program

This Python program allows you to convert images to JPEG format with reduced quality while preserving Exif metadata and handling image orientation based on Exif data. You can choose between a simple conversion or a more complex conversion that includes processing images in subdirectories.

## Prerequisites

- Python 3.x
- Pillow (Python Imaging Library, forked as Pillow)

## Usage

1. Clone or download this repository to your local machine.

2. Ensure you have Python 3.x installed. You can download it from the official Python website: https://www.python.org/downloads/

3. Install the Pillow library if you haven't already. You can install it using pip:

   ```bash
   pip install Pillow
Run the program using the following command:
bash
Copy code
python main.py
This will launch the program and provide you with the following options:
Simple Conversion: Converts images in a single directory.
Complex Conversion: Recursively processes images in a directory and its subdirectories.
Select the option by entering "1" or "2" based on your choice.
For Simple Conversion:
Enter the input directory path.
Enter the output directory path.
For Complex Conversion:
Enter the input directory path.
Enter the output directory path.
The program will convert the images and save them in the specified output directory.
Notes

The program will handle Exif orientation data to correctly orient the images.
You can adjust the image quality by modifying the quality parameter in the code.
License

This program is provided under the MIT License. See the LICENSE file for more details.

csharp
Copy code

You can save this content in a file named `README.md` in the root directory of your project. You can also add more details or customize it further as needed.
