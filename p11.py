#!/usr/bin/env python3

from common import splitLines

INPUT = 'input11.txt'

def task1():
    answer = 0
    items = 0
    for line in splitLines(INPUT, ' ')[:-1]:
        for word in line:
            if word == 'a':
                items += 1
        answer += 2*items - 3
    return answer

def task2():
    answer = 0
    items = 0
    for line in splitLines('input11b.txt', ' ')[:-1]:
        for word in line:
            if word == 'a' or word == 'an':
                items += 1
        answer += 2*items - 3
    return answer

print(task1())
print(task2())
