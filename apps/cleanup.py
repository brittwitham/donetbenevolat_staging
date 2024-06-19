import subprocess
import argparse
import ast
import os

def format_code(directory):
    command = f'autopep8 --in-place --aggressive --aggressive --recursive {directory}'
    subprocess.run(command, shell=True, check=True)

def run_pylint(directory):
    command = f'pylint {directory}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result

def check_return_statements(file_path):
    with open(file_path, 'r') as source:
        tree = ast.parse(source.read(), filename=file_path)

    functions_without_return = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not any(isinstance(n, ast.Return) for n in node.body):
                functions_without_return.append(node.name)
    
    if functions_without_return:
        print(f'❌ Functions without return statement in {file_path}: {functions_without_return}')
    else:
        print(f"✅ All funcitons in {file_path} have a return statement")


def main():
    parser = argparse.ArgumentParser(description="Format code and output Pylint score.")
    
    # Add argument for the format operation
    parser.add_argument('--format_directory', required=True, help='The directory to format using autopep8.')

    args = parser.parse_args()

    # Check return statements in 'data_utils.py'
    data_utils_path = os.path.join(args.format_directory, 'data_utils.py')
    if os.path.exists(data_utils_path):
        check_return_statements(data_utils_path)
    else:
        print(f"File '{data_utils_path}' does not exist.")

    # Format code
    format_code(args.format_directory)
    print("✅ Code formatted")

    # Run Pylint and get score
    pylint_result = run_pylint(args.format_directory)
    pylint_score = pylint_result.stdout.splitlines()[-2]  # Assuming the score is in the second last line
    print(f"Pylint score: {pylint_score}")

if __name__ == "__main__":
    main()
