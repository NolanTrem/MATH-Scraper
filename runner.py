"""
Creates a CSV file with the MATH dataset problems.
"""

import csv
import json
import os
from typing import List


def get_math_problems(level: str = None) -> List[dict]:
    """
    Returns a list of math problems from the MATH dataset.
    Produced in a round-robin fashion from each category to allow for an
    even distribution over n-samples.
    """
    base_path = "MATH/test"

    category_problems = {}
    categories = [
        "algebra",
        "counting_and_probability",
        "geometry",
        "intermediate_algebra",
        "number_theory",
        "prealgebra",
        "precalculus",
    ]

    for category in categories:
        category_path = os.path.join(base_path, category)

        if os.path.isdir(category_path):
            sorted_file_names = sorted(
                os.listdir(category_path), key=lambda x: int(os.path.splitext(x)[0])
            )

            category_problems[category] = []
            for file_name in sorted_file_names:
                file_path = os.path.join(category_path, file_name)
                with open(file_path, "r") as f:
                    problem_details = json.load(f)

                    if level is None or problem_details.get("level") == level:
                        new_problem = {
                            "id": os.path.splitext(file_name)[0],
                            "problem": problem_details.get("problem"),
                            "level": problem_details.get("level"),
                            "type": problem_details.get("type"),
                            "solution": problem_details.get("solution"),
                        }
                        category_problems[category].append(new_problem)

    problems_list = []
    while any(category_problems.values()):
        problems_list.extend(
            category_problems[category].pop(0)
            for category in categories
            if category_problems[category]
        )

    return problems_list


def save_to_csv(problems: List[dict], output_file: str = "problems.csv"):
    """Save the problems list into a CSV file."""
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["id", "problem", "level", "type", "solution"]
        )
        writer.writeheader()
        for problem in problems:
            writer.writerow(problem)


if __name__ == "__main__":
    problems = get_math_problems()
    save_to_csv(problems, "MATH_dataset_full_testing.csv")
