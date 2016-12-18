#!/usr/bin/env python3

import re

def splitLines(filename, expression):
    exp = re.compile(expression)
    lines = []
    with open(filename) as fd:
        for line in fd:
            parts = re.split(exp, line.strip())
            lines.append(parts)
    return lines

INPUT = 'input15b.txt'


def find_time(input_file):
    disks = []

    for line in splitLines(input_file, ' '):
        disks.append((int(line[3]),int(line[11].strip('.'))))

    for time in range(1000000000):
        if sum([(time+k+1+v[1]) % v[0] for k,v in enumerate(disks)]) > 0:
            continue
        return time
        break

def task1():
    return find_time('input15.txt')

def task2():
    return find_time('input15b.txt')

if __name__ == '__main__':
    print(task1())
    print(task2())
