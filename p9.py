#!/usr/bin/env python3

INPUT = 'input9.txt'

import re

data = ''

with open(INPUT) as fd:
    data = ''.join(re.split('\s', fd.read()))

def task1(data):
    output = ''
    while True:
        match = re.search('\(([0-9]+)x([0-9]+)\)', data)
        if match:
            output += data[:match.start()]

            span = int(match.group(1))
            repeat = int(match.group(2))

            output += repeat*data[match.end():match.end()+span]

            data = data[match.end()+span:]
        else:
            output += data
            break

    return len(output)

def task2(data):
    count = 0
    while True:
        match = re.search('\(([0-9]+)x([0-9]+)\)', data)
        if match:
            count += match.start()

            span = int(match.group(1))
            repeat = int(match.group(2))

            inner_count = task2(data[match.end():match.end()+span])

            count += repeat*inner_count

            data = data[match.end()+span:]
        else:
            count += len(data)
            break

    return count

print(task1(data))
print(task2(data))
