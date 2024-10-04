#!/usr/bin/python3
import csv
import json
from pyparsing import White


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.
    Returns True if successful, False if the CSV file is not found.
    """
    json_data = []

    '''Open the CSV file for reading'''
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        '''Create a CSV reader object'''
        csv_reader = csv.DictReader(csv_file)

        '''Iterate through each row in the CSV file'''
        for row in csv_reader:
            json_data.append(row)

    '''Write the JSON data to a file'''
    with open('data.json', mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)
