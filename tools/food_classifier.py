#! /usr/bin/env python3

import csv
import sys

try:
    input_name = sys.argv[1]
    output_expression = sys.argv[2]
    output_rest = sys.argv[3]
    expression = sys.argv[4]

except:
    print('Usage: input.csv output.csv')
    exit()

with open(input_name, newline='') as csvinput_file:
    with open(output_expression, 'w', newline='') as csvoutput_file_expression:
        with open(output_rest, 'w', newline='') as csvoutput_file_rest:
            db_spreadsheet = csv.reader(csvinput_file, delimiter='\t', quotechar='"')
            db_output_expression = csv.writer(csvoutput_file_expression, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            db_output_rest = csv.writer(csvoutput_file_rest, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in db_spreadsheet:
                if row[1].find(expression) != -1:
                    db_output_expression.writerow(row)
                else:
                    db_output_rest.writerow(row)