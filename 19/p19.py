#!/usr/bin/env python3

# It's a variation on the Josephus problem

INPUT = 3004953

def opposite(elf, elfs):
    return (int) ((elf + (elfs/2)) % elfs)

def task1(elves = INPUT):
    # With two elves, zero (the one who steals) wins
    winner = 0
    # Count backwards to find what position that elf had
    # when there were 3, 4, 5, ... elves left
    for i in range(2, elves+1):
        winner = (winner + 2) % i
    # Return 1-indexed elf, winner is zero-indexed
    return winner + 1

def task2(elves = INPUT):
    # With two elves, zero wins
    winner = 0
    # Count backwards to add more elves
    for i in range(2, elves + 1):
        # The stealing elf moved a step to the left last time, so
        # the winner must have been at least one more step away.
        winner = (winner + 1) % i
        # If an elf between the current stealer and the winner is about
        # to be robbed, that would have changed the outcome of the previous
        # round, so the robbed elf must have been in that range too.
        # Move two steps away to accomodate the newly robbed elf.
        if opposite(0, i) <= winner:
            winner = (winner + 1) % i
    return winner + 1

print(task1())
print(task2())
