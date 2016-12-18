#!/usr/bin/env python3

import itertools

INPUT = 'input18.txt'

def get_input():
    with open(INPUT) as fd:
        return '.' + fd.readline().strip() + '.'

def genlines(line):
    while True:
        yield line
        newline = '.'
        for k in range(1, len(line)-1):
            linebit = line[k-1:k+2]
            if linebit == '^^.' or linebit == '.^^' \
               or linebit == '^..' or linebit == '..^':
                newline += '^'
            else:
                newline += '.'
        line = newline + '.'

def task(rows):
    return sum([l.count('.') - 2
                for l in itertools.islice(genlines(get_input()), rows)])
def task1():
    return task(40)

def task2():
    return task(400000)

print(task1())
print(task2())
