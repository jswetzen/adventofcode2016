#!/usr/bin/env python3

import operator

data = open('input6.txt')

common = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

for line in data:
    i = 0
    for char in line:
        try:
            common[i][char] = common[i][char] + 1
        except KeyError:
            common[i][char] = 1
        i = i + 1

most_common = ""
for pos in common:
    most_common += max(pos.keys(), key=(lambda key: pos[key]))[0]

least_common = ""
for pos in common:
    least_common += min(pos.keys(), key=(lambda key: pos[key]))[0]

print(least_common)
