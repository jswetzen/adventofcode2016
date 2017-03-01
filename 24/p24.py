#!/usr/bin/env python3

"""
It's not efficient, but it's a hamiltonian path problem and there are only a
few locations to consider.
"""

import queue
import itertools

INPUT = 'input24.txt'

def print_map(locations):
    for y in range(len(locations[0])):
        for x in range(len(locations)):
            print(locations[x][y], end='')
        print('')

def read_input():
    with open(INPUT) as data:
        lines = list(map(lambda line: line.strip(), data.readlines()))
        return (len(lines[0]), len(lines), list(map(list, zip(*lines))))

def moves(locations, pos):
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    options = []
    for x, y in [tuple(map(sum, zip(pos, delta))) for delta in dirs]:
        if locations[x][y] is not '#' and locations[x][y] is not ' ':
            if not locations[x][y].isdigit():
                locations[x][y] = ' '
            options.append((x, y))
    return options

def reset_locations(locations):
    for x in range(len(locations)):
        for y in range(len(locations[0])):
            if locations[x][y] is ' ':
                locations[x][y] = '.'

def breadth_first_dists(locations, start):
    min_dists = [100000]*10
    q = queue.Queue()
    q.put((0, start))
    while not q.empty():
        dist, (x, y) = q.get()
        [q.put((dist+1, p)) for p in moves(locations, (x, y))]
        char = locations[x][y]
        if char.isdigit() and dist < min_dists[int(char)]:
            min_dists[int(char)] = dist
    return min_dists

def find_numbers(width, height, locations):
    numbers = {}
    for x in range(width):
        for y in range(height):
            if locations[x][y].isdigit():
                numbers[int(locations[x][y])] = (x, y)
    return numbers

def find_shortest(go_back=False):
    width, height, locations = read_input()
    # print_map(locations)
    numbers = find_numbers(width, height, locations)
    # print(numbers)
    # print(moves(locations, numbers[0]))
    dists = [0]*len(numbers)
    for number, pos in numbers.items():
        dists[number] = breadth_first_dists(locations, pos)
        reset_locations(locations)
    min_dist = 10000000
    for order in itertools.permutations(range(1,len(numbers))):
        dist, last = (0, 0)
        for pos in order:
            dist += dists[last][pos]
            last = pos
        if go_back:
            dist += dists[last][0]
        if min_dist > dist:
            min_dist = dist
            best_order = order
    return min_dist

def task1():
    return find_shortest(False)

def task2():
    return find_shortest(True)

answer1 = task1()
assert(answer1 == 518)
print(answer1)
answer2 = task2()
assert(answer2 == 716)
print(answer2)
