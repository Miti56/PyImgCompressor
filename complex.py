import argparse
from PIL import Image, ExifTags
import os
import shutil


def convert_images(input_folder, output_folder):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            # Convert the filename to lowercase for case-insensitive matching
            lowercase_filename = filename.lower()
            if lowercase_filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)
                output_dir = os.path.dirname(output_path)

                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                try:
                    img = Image.open(input_path)

                    # Use PIL to handle Exif orientation
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            break
                    exif = dict(img._getexif().items())

                    if exif.get(orientation) == 3:
                        img = img.rotate(180, expand=True)
                    elif exif.get(orientation) == 6:
                        img = img.rotate(270, expand=True)
                    elif exif.get(orientation) == 8:
                        img = img.rotate(90, expand=True)

                    # Copy Exif metadata to the new image
                    if "exif" in img.info:
                        exif_data = img.info["exif"]
                        img.save(output_path, 'JPEG', quality=50, exif=exif_data)
                    else:
                        img.save(output_path, 'JPEG', quality=50)

                    print(f'Converted {input_path} to {output_path}')
                except Exception as e:
                    print(f'Error converting {input_path}: {str(e)}')


def main():
    print("Image Conversion Script")
    input_directory = input("Enter the input directory path: ")
    output_directory = input("Enter the output directory path: ")

    if not os.path.exists(input_directory):
        print(f'Directory not found: {input_directory}')
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    convert_images(input_directory, output_directory)


if __name__ == '__main__':
    main()
