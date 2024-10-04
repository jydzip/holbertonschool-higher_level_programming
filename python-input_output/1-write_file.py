#!/usr/bin/python3
"""
    function to write a text file
"""


def write_file(filename="", text=""):
    '''Use 'with' to open the file in write mode'''
    with open(filename, 'w', encoding='UTF-8') as file:
        '''
            Write the text to the file and
            return the number of characters written
        '''
        return file.write(text)
