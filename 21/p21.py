#!/usr/bin/env python3
"""
I didn't solve this in the morning, and that made me attack the problem in a
different way! Testing each function against the example was nice because the
solution was correct straight away, but it took a long time to copy those
tests...
"""

import doctest
import itertools

INPUT = 'input21.txt'

def splitLines(filename, exp):
    with open(filename) as fd:
        return [line.strip().split(exp) for line in fd]

def swap_pos(passw, i1, i2):
    """
    >>> ''.join(swap_pos(list('abcde'), 4, 0))
    'ebcda'
    """
    char = passw[i1]
    passw[i1] = passw[i2]
    passw[i2] = char
    return passw

def swap_char(char, l1, l2):
    """
    >>> swap_char('a', 'a', 'b')
    'b'
    >>> swap_char('b', 'a', 'b')
    'a'
    >>> swap_char('c', 'a', 'b')
    'c'
    """
    if char == l1:
        return l2
    elif char == l2:
        return l1
    else:
        return char

def swap_letter(passw, l1, l2):
    """
    >>> ''.join(swap_letter(list('ebcda'), 'd', 'b'))
    'edcba'
    """
    return [swap_char(c, l1, l2) for c in passw]

def rotate_dir(passw, right, steps):
    """
    >>> ''.join(rotate_dir(list('abcde'), False, 1))
    'bcdea'
    >>> ''.join(rotate_dir(list('abcde'), True, 2))
    'deabc'
    """
    steps = steps % len(passw)
    if right:
        return passw[len(passw) - steps:] + passw[:len(passw) - steps]
    else:
        return passw[steps:] + passw[:steps]

def rotate_pos(passw, char):
    """
    >>> ''.join(rotate_pos(list('abdec'), 'b'))
    'ecabd'
    >>> ''.join(rotate_pos(list('ecabd'), 'd'))
    'decab'
    """
    steps = 1 + passw.index(char)
    if steps > 4:
        steps += 1
    return rotate_dir(passw, True, steps)

def reverse(passw, i1, i2):
    """
    >>> ''.join(reverse(list('edcba'), 0, 4))
    'abcde'
    """
    middle = passw[i1:i2+1]
    middle.reverse()
    return passw[:i1] + middle + passw[i2+1:]

def move(passw, i1, i2):
    """
    >>> ''.join(move(list('bcdea'), 1, 4))
    'bdeac'
    >>> ''.join(move(list('bdeac'), 3, 0))
    'abdec'
    """
    char = passw[i1]
    del passw[i1]
    passw.insert(i2, char)
    return passw

def scramble(operations, password='abcdefgh'):
    password = list(password)
    for op in operations:
        cmd = op[0] + ' ' + op[1]
        if cmd == 'swap position':
            password = swap_pos(password, int(op[2]), int(op[5]))
        elif cmd == 'swap letter':
            password = swap_letter(password, op[2], op[5])
        elif cmd == 'rotate left' or cmd == 'rotate right':
            password = rotate_dir(password, op[1] == 'right', int(op[2]))
        elif cmd == 'rotate based':
            password = rotate_pos(password, op[6])
        elif cmd == 'reverse positions':
            password = reverse(password, int(op[2]), int(op[4]))
        elif cmd == 'move position':
            password = move(password, int(op[2]), int(op[5]))

    return ''.join(password)

def task1():
    """
    >>> task1()
    'bdfhgeca'
    """
    return scramble(splitLines(INPUT, ' '))

def task2():
    """
    A "slow" brute force solution (two seconds),
    but it only took two minutes to write!
    >>> task2()
    'gdfcabeh'
    """
    password = 'fbgdceah'
    operations = splitLines(INPUT, ' ')

    for cleartext in itertools.permutations(password):
        if scramble(operations, cleartext) == password:
            return ''.join(cleartext)
    return None

if __name__ == "__main__": 
    doctest.testmod()
    print(task1())
    print(task2())

