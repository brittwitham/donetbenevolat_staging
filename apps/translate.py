import csv
import os
from pathlib import Path
import re

# Path to the CSV file and your repository
csv_file_path = 'translations.csv'
repo_path = '/Users/brittany/repos/donetbenevolat/apps'

csv_files_to_process = [
    '/Users/brittany/repos/donetbenevolat/tables/empGrowth.csv',
    '/Users/brittany/repos/donetbenevolat/tables/empGrowthActivity.csv',
    '/Users/brittany/repos/donetbenevolat/tables/empSubSec.csv',
    '/Users/brittany/repos/donetbenevolat/tables/empSubSecActivity.csv',
    '/Users/brittany/repos/donetbenevolat/tables/gdpGrowth.csv',
    '/Users/brittany/repos/donetbenevolat/tables/gdpSubSec.csv',
    '/Users/brittany/repos/donetbenevolat/tables/gdpSubSecActivity.csv',
    '/Users/brittany/repos/donetbenevolat/tables/jobsDemog.csv',
    '/Users/brittany/repos/donetbenevolat/tables/jobsType.csv',
    '/Users/brittany/repos/donetbenevolat/tables/perNatGDP.csv',
    '/Users/brittany/repos/donetbenevolat/tables/revGrowth.csv',
    '/Users/brittany/repos/donetbenevolat/tables/revGrowthActivity.csv',
    '/Users/brittany/repos/donetbenevolat/tables/revGrowthSource.csv',
    '/Users/brittany/repos/donetbenevolat/tables/revSource.csv',
    '/Users/brittany/repos/donetbenevolat/tables/revSubSec.csv',
    '/Users/brittany/repos/donetbenevolat/tables/revSubSecActivity.csv',
    '/Users/brittany/repos/donetbenevolat/tables/wagesDemog.csv',
    '/Users/brittany/repos/donetbenevolat/tables/wagesType.csv'
]

# Read the CSV and store the replacements in a dictionary
replacements = {}
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        replacements[row['EN']] = row['FR']

# Function to replace phrases in 'graphs.py' files
def replace_phrases_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for en, fr in replacements.items():
        pattern = r'\b{}\b'.format(re.escape(en))
        content = re.sub(pattern, fr, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Function to replace phrases in a CSV file
def replace_phrases_in_csv(file_path):
    # Read the CSV file into a list of dictionaries
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
        headers = reader.fieldnames

    # Perform the replacements
    for row in rows:
        for header in headers:
            for en, fr in replacements.items():
                # Use regex to replace only whole words
                pattern = r'\b{}\b'.format(re.escape(en))
                row[header] = re.sub(pattern, fr, row[header])

    # Write the modified content back to the CSV
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

# Process 'graphs.py' files in the repository
for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file in ('callbacks.py', 'graphs.py'):
        # if file == 'graphs.py':
            replace_phrases_in_file(Path(root) / file)

# # Process each CSV file
# for csv_file in csv_files_to_process:
#     replace_phrases_in_csv(csv_file)

print("Phrase replacement complete.")

