#!/usr/bin/python3
import json
import csv


def convert_csv_to_json(filename):
    try:
        OUTPUT = filename.replace(".csv", ".json")
        data = []
        with open(filename, "r") as fc:
            reader = csv.DictReader(fc)
            for row in reader:
                data.append(row)
        with open(OUTPUT, "w") as f:
            f.write(json.dumps(data, indent=4))
    except Exception:
        return False
    return True
