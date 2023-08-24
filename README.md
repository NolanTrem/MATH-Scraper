# MATH-Scraper

MATH-Scraper is a dataset tool designed to generate CSVs from the "MATH" Dataset by Hendrycks et al. It facilitates the conversion of individual JSON problem files from the dataset into a consolidated CSV format. Problems are collected in a round-robin fashion from each category, ensuring an even distribution over the samples.

## Features:

- Extracts problems from the MATH dataset.
- Consolidates problems into a single CSV file.
- Ensures an even distribution of problems by processing them in a round-robin fashion.

## Setup and Installation:

1. Ensure you have [Poetry](https://python-poetry.org/docs/) installed. If not, [install Poetry](https://python-poetry.org/docs/#installation).
2. Navigate to the root directory of the project and run:
    ```bash
    poetry install
    ```

## How to Run:
1. Activate the poetry environment:
    ```bash
    poetry shell
    ```
2. Simply run the runner.py script:
    ```bash
    python runner.py
    ```
The script will generate a CSV named `MATH_dataset_full_testing.csv` containing the problems.

## Contributing:
Feel free to fork the repository and submit pull requests for any enhancements or fixes. Feedback and contributions are always welcome.
