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

def get(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]

def run(lines, regs, limit):
    pos = 0
    out = []
    while pos < len(lines) and limit > 0:
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
        elif lines[pos][0] == 'out':
            out.append(get(lines[pos][1]))
            pos += 1
            limit -= 1
    # print(out)
    return out

INPUT = 'input25.txt'

lines = splitLines(INPUT, '\s')

for i in range(189, 10000000):
    # print("Try {}".format(i))

    regs = {'a': i, 'b': 0, 'c': 0, 'd': 0}

    out_len = 10
    output = run(lines, regs, out_len)
    if len(output) != out_len:
        print("WRONG")
        break
    if sum(output[1::2]) == (out_len/2) and sum(output[0::2]) == 0:
        print(i)
        # print("Got clock")
        break
