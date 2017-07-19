#! /usr/bin/env python3

import csv
import sys

file = sys.argv[1]

with open(file, newline='') as csvfile:
    db_spreadsheet = csv.reader(csvfile, delimiter='\t', quotechar='"')
