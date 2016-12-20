#!/usr/bin/env python3

INPUT = 'input20.txt'

def splitLines(filename, exp):
    with open(filename) as fd:
        return [line.strip().split(exp) for line in fd]

def task1(lines):
    lowest = 0
    for (l, h) in lines:
        if l <= lowest + 1:
            lowest = max(lowest, h)
        else:
            return lowest + 1

def task2(lines):
    allowed = 0
    lowest = 0
    for (l,h) in lines:
        if l <= lowest + 1:
            lowest = max(lowest, h)
        else:
            allowed += l - lowest - 1
            lowest = h
    return allowed

lines = sorted([(int(x[0]), int(x[1])) for x in splitLines(INPUT, '-')])

print(task1(lines))
print(task2(lines))
