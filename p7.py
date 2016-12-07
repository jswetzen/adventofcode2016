#!/usr/bin/env python3

INPUT = 'input7.txt'

import re

import common

def abba(string):
    match = re.match('.*(?P<fst>.)(?P<snd>.)(?P=snd)(?P=fst).*', string)
    return match and match.group('fst') != match.group('snd')

def task1():
    TLS_ips = []

    for parts in common.splitLines(INPUT, '\[|\]'):
        has_abba = False
        hyper_abba = False

        hyper = False

        for part in parts:
            if abba(part):
                if hyper:
                    hyper_abba = True
                else:
                    has_abba = True
            hyper = not hyper
        if has_abba and not hyper_abba:
            TLS_ips.append(parts)

    print(len(TLS_ips))

def abas(string, reverse):
    result = set()
    for i in range(0,len(string)-2):
        if string[i] == string[i+2] and string[i] != string[i+1]:
            if reverse:
                result.add(string[i+1]+string[i]+string[i+1])
            else:
                result.add(string[i:i+3])
    return result

def task2():
    TLS_ips = []

    for parts in common.splitLines(INPUT, '\[|\]'):
        aabas = set()
        hyper_abas = set()

        hyper = False

        for part in parts:
            if hyper:
                hyper_abas |= abas(part, True)
            else:
                aabas |= abas(part, False)
            hyper = not hyper
        if not aabas.isdisjoint(hyper_abas):
            TLS_ips.append(parts)

    print(len(TLS_ips))

task1()
task2()
