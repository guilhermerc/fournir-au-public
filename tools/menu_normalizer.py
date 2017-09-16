#! /usr/bin/env python3

import csv
import sys

try:
    input_name = sys.argv[1]
    output_name = sys.argv[2]
except: 
    print('Usage: input.csv')
    exit()

with open(input_name, newline = '') as csvinput_file:
    with open(output_name, 'w', newline = '') as csvoutput_file:
        db_input = csv.reader(csvinput_file, delimiter = '\t', quotechar = '"')
        db_output = csv.writer(csvoutput_file, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        for row in db_input:
            full_name = input_name.split('.')
            name = full_name[0]
            row[1] = name
            db_output.writerow(row)
