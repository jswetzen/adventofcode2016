#!/usr/bin/env python3

INPUT = 'input8.txt'

import re

def splitLines(filename, expression):
    exp = re.compile(expression)
    lines = []
    with open(filename) as fd:
        for line in fd:
            parts = re.split(exp, line.strip())
            lines.append(parts)
    return lines

screen = [[0 for x in range(50)] for y in range(6)]

def add_rect(screen, x, y):
    for i in range(x):
        for j in range(y):
            screen[j][i] = 1
    return screen

def shift(ary, by):
    result = [0 for x in range(len(ary))]
    for i in range(len(ary)):
        result[(i+by) % len(ary)] = ary[i]
    return result

def rotate(screen, row, index, by):
    if row:
        screen[index] = shift(screen[index], by)
    else:
        column = [screen[x][index] for x in range(len(screen))]
        column = shift(column, by)
        for x in range(len(screen)):
            screen[x][index] = column[x]
            
    return screen

def count_lit(screen):
    count = 0
    for row in screen:
        count += sum(row)
    return count

def prettyprint(screen):
    for line in screen:
        print(''.join(['#' if c == 1 else ' ' for c in line]))

def task1():
    for line in splitLines(INPUT, ' '):
        if line[0] == 'rect':
            [x,y] = line[1].split('x')
            add_rect(screen, int(x), int(y))
        elif line[0] == 'rotate':
            row = line[1] == 'row'
            index = int(line[2].split('=')[1])
            by = int(line[4])
            rotate(screen, row, index, by)

    print(count_lit(screen))

def task2():
    prettyprint(screen)
    print("AFBUPZBJPS")

task1()
task2()
