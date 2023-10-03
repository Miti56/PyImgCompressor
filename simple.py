import os
from PIL import Image, ExifTags

# Prompt the user for input and output folders
input_folder = input("Enter the input directory path: ")
output_folder = input("Enter the output directory path: ")

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to convert images in the input folder to JPEG format with reduced quality and save them in the output folder
def convert_images(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        # Convert the filename to lowercase for case-insensitive matching
        lowercase_filename = filename.lower()
        if lowercase_filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                img = Image.open(input_path)

                # Use PIL to handle Exif orientation
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break
                exif = dict(img._getexif().items())

                if exif[orientation] == 3:
                    img = img.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    img = img.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    img = img.rotate(90, expand=True)

                img.save(output_path, 'JPEG', quality=50)  # Adjust quality as needed (0-100)
                print(f'Converted {filename} to JPEG format')
            except Exception as e:
                print(f'Error converting {filename}: {str(e)}')

# Call the function to convert images
convert_images(input_folder, output_folder)
