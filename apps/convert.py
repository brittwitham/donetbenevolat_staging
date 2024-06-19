import re
import os
import sys
import shutil

# Check if the user has provided the necessary arguments
if len(sys.argv) < 3:
    print("Usage: python script_name.py input_filename output_directory")
    sys.exit(1)

input_file = sys.argv[1]
output_directory = sys.argv[2]

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Read the provided file
with open(input_file, 'r') as f:
    content = f.read()

# Mapping of section names to filenames
section_to_filename = {
    "Data processing": "data_processing.py",
    "App layout": "app_layout.py",
    "Callbacks": "callbacks.py"
}

# Split the content using the commented-out headings with at least 5 '#'
sections = re.split(r'#\s*(#####+)\s+(.*?)\s+\1\s*#', content)

# Default imports for the app_layout.py file
app_layout_imports = """from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *

register_callbacks(app)
"""

# Default imports and function for the callbacks.py file
callbacks_defaults = """import dash
from .data_processing import *
from .graphs import *

def register_callbacks(app):
"""

# Default imports for the data_processing.py file
data_processing_imports = "from .data_utils import *\n\n"

# Iterate through the sections, create new files in the specified
# directory and save the content
for i in range(1, len(sections) - 1, 3):
    # Get the file name from the mapping, else generate a filename format
    file_name = section_to_filename.get(
        sections[i + 1], sections[i + 1].lower().replace(' ', '_') + '.py')

    # Create the full path for the file
    file_path = os.path.join(output_directory, file_name)

    # Add the comment at the beginning of each section file
    section_comment = f"# {sections[i+1]} file for {os.path.basename(output_directory)} converted from {os.path.basename(input_file)}\n\n"

    # Determine additional content based on the file name
    if file_name == "app_layout.py":
        additional_content = app_layout_imports
    elif file_name == "callbacks.py":
        additional_content = callbacks_defaults
    elif file_name == "data_processing.py":
        additional_content = data_processing_imports
    else:
        additional_content = ""

    # Combine the comment, additional content, and section content
    section_content = section_comment + additional_content + sections[i + 2]

    # Write content to the file
    with open(file_path, 'w') as f:
        f.write(section_content)

# # Create (or overwrite) an empty main.py file in the specified directory
# main_file_comment = f"# Main file for {os.path.basename(output_directory)} converted from {os.path.basename(input_file)}\n"
# with open(os.path.join(output_directory, 'main.py'), 'w') as f:
#     f.write(main_file_comment)

# Copy the original input script to the target directory
# shutil.copy(input_file, output_directory)
