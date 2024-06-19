import os
import subprocess
import shutil
import argparse

def convert_python_file(input_filename, output_directory):
    command = f'python convert.py {input_filename} {output_directory}'
    subprocess.run(command, shell=True, check=True)

# Import the convert file
# Run with just this on a test file
# Qui_donne_aux_organismes_caritatifs_et_combien_2018.py WDHG_2018_FR

def copy_files(src, dest):
    dest_dir = os.path.dirname(dest)
    if not os.path.exists(dest_dir):
        raise FileNotFoundError(f"Destination directory {dest_dir} does not exist")
    # Perform copy
    shutil.copy2(src, dest)
    

# def format_code(directory):
#     command = f'autopep8 --in-place --aggressive --aggressive --recursive {directory}'
#     subprocess.run(command, shell=True, check=True)

def main():
    parser = argparse.ArgumentParser()

    # Conversion operations
    parser.add_argument("--source_file", required=True, help="The original file to be refactored")
    parser.add_argument("--target_directory", required=True, help="Target directory for refactored files")

    # Copy operations
    parser.add_argument("--copy_paths", nargs='+', required=True, help="Origins and destinations for the data and graph utils files")

    # # Add arguments for the copy operations
    # parser.add_argument('--copy_paths', nargs='+', required=True, help='List of origin and destination paths for copy operations in the format: origin1 destination1 origin2 destination2 ...')

    # # Add argument for the format operation
    # parser.add_argument('--format_directory', required=True, help='The directory to format using autopep8.')

    args = parser.parse_args()

    # Convert Python file
    convert_python_file(args.source_file, args.target_directory)

    # Copy files
    copy_file_paths = zip(args.copy_paths[::2], args.copy_paths[1::2])
    # print("Copy file paths:", list(copy_file_paths))
    for src, dest in copy_file_paths:
        copy_files(src, dest)

#     # Format code
#     format_code(args.format_directory)

if __name__ == "__main__":
    main()

# python run_conversion.py --source_file Qui_donne_aux_organismes_caritatifs_et_combien_2018.py --target_directory WDHG_2018_FR
