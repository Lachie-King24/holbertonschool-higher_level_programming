#!/usr/bin/python3
""""takes the CSV f name as parameter and writes JSON data to file"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file named data.json"""
    try:
        data = []

        with open(csv_filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except (FileNotFoundError, IOError):
        return False