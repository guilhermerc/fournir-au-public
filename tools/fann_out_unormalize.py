#! /usr/bin/env python3

import sys

normalized_number = float(sys.argv[1])

def unormalize_elem(value):
    return ((value + 0.5)*(13000 - 1000)) + 1000

print(str(unormalize_elem(normalized_number)))
