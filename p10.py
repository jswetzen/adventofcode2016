#!/usr/bin/env python3

from common import splitLines

INPUT = "input10.txt"

bots = {}
input_bins = []


class Bot:
    def __init__(self, bot_id, low_output, high_output):
        self.bot_id = bot_id
        self.low = None
        self.high = None
        self.low_output = low_output
        self.high_output = high_output
        # print("bot {} gives low to bot {} and high to bot {}"
                # .format(self.bot_id, self.low_output, self.high_output))

    def take_input(self, value):
        if self.low and value > self.low:
            self.high = value
        else:
            self.high = self.low
            self.low = value

        if self.low and self.high:
            if self.low is 17 and self.high is 61:
                print("I'm bot {} and I compare {} to {}!".format(self.bot_id,
                                                                  self.high,
                                                                  self.low))
            bots[self.low_output].take_input(self.low)
            bots[self.high_output].take_input(self.high)


class OutputBin:
    def __init__(self, bin_id):
        self.bin_id = bin_id
        self.value = None

    def take_input(self, value):
        self.value = value
        # print("I'm bin {} and I got chip {}".format(self.bin_id, self.value))

    def value(self):
        return self.value


class InputBin:
    def __init__(self, value, output_bot):
        self.value = value
        self.output_bot = output_bot
        # print("value {} goes to bot {}".format(value, output_bot))

    def deliver(self):
        bots[self.output_bot].take_input(self.value)


def build_graph(filename):
    for parts in splitLines(filename, ' *'):
        if parts[0] == 'value':
            value = int(parts[1])
            output_bot = int(parts[5])
            input_bins.append(InputBin(value, output_bot))
        elif parts[0] == 'bot':
            bot_id = int(parts[1])
            low_output = int(parts[6])
            high_output = int(parts[11])
            if parts[5] == 'output':
                low_output = "output_" + str(low_output)
                bots[low_output] = OutputBin(low_output)
            if parts[10] == 'output':
                high_output = "output_" + str(high_output)
                bots[high_output] = OutputBin(high_output)
            bots[bot_id] = Bot(bot_id, low_output, high_output)

def task1():
    build_graph(INPUT)
    for input_bin in input_bins:
        input_bin.deliver()

def task2():
    print(bots['output_0'].value*bots['output_1'].value*bots['output_2'].value)

task1()
task2()
