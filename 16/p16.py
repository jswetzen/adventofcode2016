#!/usr/bin/env python3

INPUT = '10111011111001111'
INPUT_LEN = 272
INPUT_LEN2 = 35651584
test_input = '10000'
test_len = 20

def dragon(binary):
    binary2 = ([0 if x else 1 for x in binary[::-1]])
    return binary + [0] + binary2

def expand(binstr, length):
    binary = list(map(int, binstr))
    while len(binary) < length:
        binary = dragon(binary)

    return binary[:length]

def checksum(b):
    while not (len(b) & 1):
        newb = []
        for i in range(int(len(b) / 2)):
            newb.append(1 if b[2*i] == b[2*i+1] else 0)
        b = newb
    return b

def task1():
    return checksum(expand(INPUT, INPUT_LEN))

def task2():
    return checksum(expand(INPUT, INPUT_LEN2))

if __name__ == '__main__':

    print(''.join(map(str,task1())))
    print(''.join(map(str,task2())))

