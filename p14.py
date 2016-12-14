#!/usr/bin/env python3

import hashlib
import re

def stretch_key(key, stretch=2016):
    md5 = hashlib.md5(key.encode()).hexdigest()
    for i in range(stretch):
        md5 = hashlib.md5(md5.encode()).hexdigest()
    return md5

INPUT = 'ahsbgdzn'
# INPUT = 'abc'

def solve(stretch=0):

    count = 0

    triplets = {}
    keys = []

    triplet_exp = re.compile('(?P<num>[0-9a-f])(?P=num)(?P=num)')
    five_exp = re.compile('(?P<num>[0-9a-f])(?P=num)(?P=num)(?P=num)(?P=num)')

    while len(keys) < 64 or count < keys[63]+1000:
        md5 = stretch_key(INPUT+str(count), stretch)
        match_3 = re.search(triplet_exp, md5)
        if match_3:
            char = md5[match_3.start()]
            if char in triplets:
                triplets[char].append(count)
            else:
                triplets[char] = [count]

        match_5 = re.findall(five_exp, md5)
        if match_5:
            # print("{}: {} in {}".format(count, 5*match_5[0], md5))
            # print(md5)
            for match in match_5:
                # print("{}: {} in {}".format(count, 5*match, md5))
                if match in triplets:
                    # print(triplets[match])
                    new_matches = []
                    for key, val in enumerate(triplets[match]):
                        if val+1000 < count:
                            pass
                            # print("Deleting {}, it's too low".format(val))
                        elif val != count:
                            keys.append(val)
                            keys.sort()
                            # print("{} contains {}, at {} we have {}".format(val, match,
                                # count, md5))
                        else:
                            new_matches.append(val)
                            # print("{} was not considered".format(val))
                        triplets[match] = new_matches
        count += 1

    # for k,v in enumerate(keys):
        # print(k,v)
    print(keys[63])

if __name__ == '__main__':
    solve()
    solve(2016)
