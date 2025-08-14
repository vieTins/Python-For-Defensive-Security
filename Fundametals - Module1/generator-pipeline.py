# Generator Pipeline
# Compose generator functions to read a file, strip whitespace, filter out blank lines, and yield line numbers plus text.

def read_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line
def strip_line(lines):
    for line in lines:
        yield line.strip()
def filter_blank(lines):
    for line in lines:
        if line:
            yield line 
def line_number(lines):
    for i, line in enumerate(lines, start=1): 
        yield i, line 

import os
filename = os.path.join(os.path.dirname(__file__), 'example.txt')

lines = read_line(filename)
lines = strip_line(lines)
lines = filter_blank(lines)
lines = line_number(lines)

for num, text in lines:
    print(f"{num}: {text}")
