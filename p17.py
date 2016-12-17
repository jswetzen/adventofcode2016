#!/usr/bin/env python3

import queue
import hashlib

INPUT = 'veumntbg'

def valid_pos(key, pos, v, k, md5):
    (x, y) = pos
    if md5[k] >= 'b' and md5[k] <= 'f':
        return x >= 0 and x < 4 and y >= 0 and y < 4
    else:
        return False

def open_doors(path, pos):
    dirs = ['U', 'D', 'L', 'R']
    doors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    md5 = hashlib.md5((path).encode()).hexdigest()
    options = []
    for k, v in enumerate(doors):
        new_pos = tuple(map(sum, zip(pos, v)))
        if valid_pos(path, new_pos, v, k, md5):
            options.append((dirs[k], new_pos))

    return options

def solve(input_str):
    q = queue.Queue()
    q.put((input_str, (0, 0)))

    shortest_path = ''
    longest_path_length = 0

    while not q.empty():
        (path, pos) = q.get()
        if pos == (3,3):
            if not shortest_path:
                shortest_path = path[len(input_str):]
            longest_path_length = max(longest_path_length,
                                      len(path) - len(input_str))
        else:
            [q.put((path+step, new_pos))
             for step, new_pos in open_doors(path, pos)]
    print(shortest_path)
    print(longest_path_length)

solve(INPUT)
