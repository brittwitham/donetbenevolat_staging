# StatsCan Data Portal - Staging Environment

## Usage

Install pipenv if not already installed:

`pip install --user pipenv`

Then run:

`pipenv install`

`pipenv shell` (activiates venv)

`python index.py`

And navigate to: [localhost:8050](localhost:8050)

## Structure

### apps

- Dash apps for each of the stories

### assets

- Where various web assets (such as images) are stored

### tables

- Where the raw data for the visualizations is stored

### utils

- Where functions used to generate graphs & serve data are stored

### vizes

- Contains dash apps illustrating how the final version rendered by the website must look

## Reference

| Code    | Blog Title                                           |
| ------- | ---------------------------------------------------- |
| WDA0101 | Who Donates And How Much Do They Donate?             |
| HDC0102 | How Do Canadians Donate?                             |
| UTD103  | Understanding Top Donors                             |
| WDC0105 | Why Do Canadians Give?                               |
| WKC0106 | What Keeps Canadians From Giving More?               |
| WVA0201 | Who Volunteers and How Much Time Do They Contribute? |
| UTV0203 | Understanding Top Volunteers                         |

[See full reference here.](https://docs.google.com/document/d/1eU3A8B6lnt5WAGv63xGwjQ_cgT90bfARafgWELqKmS0/edit)
