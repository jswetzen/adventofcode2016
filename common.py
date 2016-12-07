#!/usr/bin/env python3

import re

def matchRegex(filename, expression):
    prog = re.compile(expression)
    matches = []
    with open(filename) as fd:
        for line in fd:
            match = re.match(prog, line)
            if match is not None:
                if match.group() != line:
                    print(line)
                    print(match.group())
                matches.append(match)
    return matches

def splitLines(filename, expression):
    exp = re.compile(expression)
    lines = []
    with open(filename) as fd:
        for line in fd:
            parts = re.split(exp, line)
            lines.append(parts)
    return lines
