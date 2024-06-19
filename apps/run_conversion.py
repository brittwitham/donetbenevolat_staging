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
    

def construct_parameters(target_directory, original_code):
    copy_paths = [
        f"/Users/britt/repos/donetbenevolat/utils/data/{original_code}_data_utils.py",
        f"/Users/britt/repos/donetbenevolat/apps/{target_directory}/data_utils.py",
        f"/Users/britt/repos/donetbenevolat/utils/graphs/{original_code}_graph_utils.py",
        f"/Users/britt/repos/donetbenevolat/apps/{target_directory}/graphs.py"
    ]
    return copy_paths

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--original_file', required=True, help='The original file to be converted.')
    parser.add_argument('--target_directory', required=True, help='The target directory for the converted file.')
    parser.add_argument('--original_code', required=True, help='The original code identifier for the file paths.')
    args = parser.parse_args()

    # Construct the parameters
    copy_paths = construct_parameters(args.target_directory, args.original_code)

    # Convert Python file
    convert_python_file(args.original_file, args.target_directory)

    # Copy files
    copy_file_paths = zip(copy_paths[::2], copy_paths[1::2])
    # print("Copy file paths:", list(copy_file_paths))
    for src, dest in copy_file_paths:
        copy_files(src, dest)


if __name__ == "__main__":
    main()

# python run_conversion.py --source_file Qui_donne_aux_organismes_caritatifs_et_combien_2018.py --target_directory WDHG_2018_FR
