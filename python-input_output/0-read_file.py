#!/usr/bin/python3
"""
    function to read a text file
"""


def read_file(filename=""):
    '''Open the file using the 'with' statement'''
    with open(filename, "r", encoding="utf-8") as file:
        '''Read the content and print it'''
        print(file.read(), end='')
