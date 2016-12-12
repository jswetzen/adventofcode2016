#!/usr/bin/env python3

from common import splitLines

INPUT = 'input12.txt'

lines = splitLines(INPUT, '\s')

pos = 0

regs = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

def get(x):
        try:
            return int(lines[pos][1])
        except ValueError:
            return regs[lines[pos][1]]

while pos < len(lines):
    if lines[pos][0] == 'cpy':
        val = get(lines[pos][1])
        regs[lines[pos][2]] = val
        pos += 1        
    elif lines[pos][0] == 'inc':
        regs[lines[pos][1]] += 1
        pos += 1        
    elif lines[pos][0] == 'dec':
        regs[lines[pos][1]] -= 1
        pos += 1        
    elif lines[pos][0] == 'jnz':
        if get(lines[pos][1]) != 0:
            pos += int(lines[pos][2])
        else:
            pos += 1

print(regs['a'])
