import subprocess


def run_simple_conversion(input_folder, output_folder):
    subprocess.run(["python", "simple.py", input_folder, output_folder], check=True)


def run_complex_conversion(input_folder, output_folder):
    subprocess.run(["python", "complex.py", input_folder, output_folder], check=True)


def main():
    print("Image Conversion Script")
    print("1. Simple Conversion")
    print("2. Complex Conversion")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        input_folder = input("Enter the input directory path for simple conversion: ")
        output_folder = input("Enter the output directory path for simple conversion: ")
        run_simple_conversion(input_folder, output_folder)
    elif choice == "2":
        input_folder = input("Enter the input directory path for complex conversion: ")
        output_folder = input("Enter the output directory path for complex conversion: ")
        run_complex_conversion(input_folder, output_folder)
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == '__main__':
    main()
