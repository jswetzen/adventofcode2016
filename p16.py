#!/usr/bin/env python3

INPUT = '10111011111001111'
INPUT_LEN = 272
INPUT_LEN2 = 35651584
test_input = '10000'
test_len = 20

def dragon(binary):
    binary2 = ''.join([ '1' if x is '0' else '0' for x in reversed(binary) ])
    return binary + '0' + binary2

def expand(binary, length):
    while len(binary) < length:
        binary = dragon(binary)

    return binary[:length]

def checksum(b):
    while len(b) % 2 is 0:
        newb = ''
        for k,v in enumerate(b[:-1]):
            if k % 2 == 1:
                continue
            if v == b[k+1]:
                newb += '1'
            else:
                newb += '0'
        b = newb
    return b

def task1():
    return checksum(expand(INPUT, INPUT_LEN))

def task2():
    return checksum(expand(INPUT, INPUT_LEN2))

if __name__ == '__main__':

    print(task1())
    print(task2())

