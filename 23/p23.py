#!/usr/bin/env python3

# The fixed input uses add and mul
INPUT = 'input23_fixed.txt'

def splitLines(filename, exp):
    lines = []
    with open(filename) as fd:
        for line in fd:
            parts = line.strip().split(exp)
            lines.append(parts)
    return lines

def get(x, regs):
        try:
            return int(x)
        except ValueError:
            return regs[x]
def toggle(cmd):
    if cmd == 'inc':
        return 'dec'
    elif cmd == 'dec' or cmd == 'tgl':
        return 'inc'
    elif cmd == 'jnz':
        return 'cpy'
    else:
        return 'jnz'

def run(lines, regs):
    pos = 0
    while pos < len(lines):
        # print(lines[pos])
        # print(regs)
        if lines[pos][0] == 'cpy':
            try:
                val = get(lines[pos][1], regs)
                regs[lines[pos][2]] = val
            except ValueError:
                pass
            pos += 1        
        elif lines[pos][0] == 'inc':
            regs[lines[pos][1]] += 1
            pos += 1        
        elif lines[pos][0] == 'dec':
            regs[lines[pos][1]] -= 1
            pos += 1        
        elif lines[pos][0] == 'add':
            regs[lines[pos][1]] += get(lines[pos][2], regs)
            pos += 1
        elif lines[pos][0] == 'mul':
            regs[lines[pos][1]] *= get(lines[pos][2], regs)
            pos += 1
        elif lines[pos][0] == 'jnz':
            if get(lines[pos][1], regs) != 0:
                # print("Jmp {} {}".format(get(lines[pos][1], regs), get(lines[pos][2], regs)))
                try:
                    pos += get(lines[pos][2], regs)
                except ValueError:
                    pos += 1
            else:
                pos += 1
        elif lines[pos][0] == 'tgl':
            # print("Cmd '{}' at {}".format(lines[pos], pos))
            offset = get(lines[pos][1], regs)
            # print("Got offset {}, changing {}".format(offset, pos+offset))
            try:
                lines[pos+offset][0] = toggle(lines[pos+offset][0])
            except (ValueError, IndexError):
                pass
            pos += 1
        elif lines[pos][0] == 'out':
            # print(get(lines[pos][1], regs))
            pos += 1

    return regs['a']

def task1(infile):
    lines = splitLines(infile, ' ')
    regs = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    return run(lines, regs)

def task2(infile):
    lines = splitLines(infile, ' ')
    regs = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    return run(lines, regs)

if __name__ == '__main__':
    assert(task1(INPUT) == 10152)
    assert(task2(INPUT) == 479006712)
    print(task1(INPUT))
    print(task2(INPUT))
