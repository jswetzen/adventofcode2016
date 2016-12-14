#!/usr/bin/env python3

import queue

INPUT = 1362
goal_x = 31
goal_y = 39

SIZE = 40

graph = {}

def wall(x, y, fav=INPUT):
    num = x*x + 3*x + 2*x*y + y + y*y + fav
    binary = "{0:b}".format(num)
    odd = binary.count('1') % 2 == 1
    return odd

def name(*args):
    return ','.join([str(arg) for arg in args])

def print_room(goal_x, goal_y, fav=INPUT, width=SIZE, height=SIZE):
    for y in range(height):
        line = ''
        for x in range(width):
            if x is goal_x and y is goal_y:
                line += '*'
            else:
                line += '#' if wall(x, y, fav) else ' '
        print(line)

def find_dist(graph, start, end, dists):
    if not start in dists:
        dists[start] = 0
    if start == end:
        return dists
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in dists:
            dists[node] = dists[start] + 1
        else:
            dists[node] = min(dists[node],dists[start]+1)
    for node in graph[start]:
        if dists[node] >= dists[start]+1:
            find_dist(graph, node, end, dists)
    return dists

def print_graph_dists(graph, dists, goal_x, goal_y):
    for y in range(SIZE):
        line = ''
        for x in range(SIZE):
            if x is goal_x and y is goal_y:
                line += '**'
            elif name(x,y) in dists:
                line += '{:>2}'.format(dists[name(x,y)])
            elif name(x,y) in graph:
                line += '  '
            else:
                line += '##'
        print(line)

def main():
    print_room(goal_x, goal_y)
    print('--------------------------------')

    # Build graph
    for y in range(SIZE):
        for x in range(SIZE):
            adj = []
            for (i,j) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if not wall(i,j):
                    adj.append(name(i,j))
            if not wall(x,y) and adj:
                graph[name(x,y)] = adj


    dists = find_dist(graph, name(1,1), name(goal_x,goal_y), {})
    print_graph_dists(graph, dists, goal_x, goal_y)

    print(dists[name(goal_x, goal_y)])
    print(len([x for x in dists.values() if x <= 50]))

if __name__ == '__main__':
    main()
