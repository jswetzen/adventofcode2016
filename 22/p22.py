#!/usr/bin/env python3

"""
This is not nice at all, but I'm solving it two months late anyway and just
want to get it done ;)
"""

import re

INPUT = 'input22.txt'

def splitLines(filename, expression):
    exp = re.compile(expression)
    lines = []
    with open(filename) as fd:
        for line in fd:
            parts = re.split(exp, line.strip())
            lines.append(parts)
    return lines

def name(*args):
    return ','.join([str(arg) for arg in args])

def parse_nodes(input_file=INPUT):
    nodes = {}

    for node in splitLines(INPUT, '[ ]*')[2:]:
        [_, x, y] = node[0].split('-')
        x = int(x[1:])
        y = int(y[1:])
        size = int(node[1][:-1])
        used = int(node[2][:-1])
        avail = int(node[3][:-1])
        nodes[name((x,y))] = {'size': size, 'used': used, 'avail': avail}
    return nodes

def task1():
    nodes = parse_nodes()
    viable = []

    nodes_by_used = sorted(nodes.items(), key=lambda x: x[1]['used'])

    for na in sorted(nodes.items(), key=lambda x: x[1]['avail']):
        for nu in nodes_by_used:
            if nu[1]['used'] <= na[1]['avail']:
                if na[0] != nu[0] and nu[1]['used'] != 0:
                    viable.append((nu[0], na[0]))
            else:
                break

    return len(viable)

def can_move(nodes, move_func, pos, new_pos, reverse=False):
    if name(pos) in nodes and name(new_pos) in nodes:
        if reverse:
            return move_func(nodes, new_pos, pos)
        else:
            return move_func(nodes, pos, new_pos)

def big_node(nodes, from_pos, to_pos):
    return nodes[name(from_pos)]['used'] < 100

def moves(nodes, move_func, path_len, pos, reverse=False):
    paths = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    options = []
    for k, v in enumerate(paths):
        new_pos = tuple(map(sum, zip(pos, v)))
        if can_move(nodes, move_func, pos, new_pos, reverse):
            options.append((path_len+1, new_pos))

    return options

def show_all(nodes):
    for i in range(31):
        print(''.join([show(nodes, pos) for pos in zip(range(32),[i]*32)]))

def show(nodes, pos):
    if pos == (0, 0):
        return '(.)'
    elif pos == (31, 0):
        return ' G '
    elif nodes[name(pos)]['used'] == 0:
        return ' _ '
    elif len(moves(nodes, big_node, 0, pos)) == 0:
        return ' # '
    else:
        #print(pos, moves(nodes, 0, pos))
        return ' . '

def find_empty(nodes):
    for i in range(31):
        for pos in zip(range(32),[i]*32):
            if nodes[name(pos)]['used'] == 0:
                return pos

def move_to_top(nodes, pos):
    steps = 0
    x, y = pos
    while y > 0:
        steps += 1
        if nodes[name((x, y-1))]['used'] > nodes[name((x, y))]['size']:
            x -= 1
        else:
            y -= 1
    return (steps, x)

def task2():
    nodes = parse_nodes()
    (empty_x, empty_y) = find_empty(nodes)
    # Move empty to top
    steps, x = move_to_top(nodes, (empty_x, empty_y))
    # Move empty next to goal
    steps += 32 - x - 2
    # Move goal to (0, 0)
    steps += 30 * 5 + 1

    return steps

assert(task1() == 985)
print(task1())

assert(task2() == 179)
print(task2())

