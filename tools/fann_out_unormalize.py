#! /usr/bin/env python3

import sys

def unormalize_elem(value):
    return ((value + 0.5)*(13000 - 1000)) + 1000

for normalized_number in sys.stdin:
    print(str(unormalize_elem(float(normalized_number))))
