#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from assertpy import assert_that

""" Day one, challenge one for dowenb's attempt at the Advent of Code 2019 Challenge
https://adventofcode.com/2019/day/1
"""

def module_fuel(mass):
    """ Take mass, divide by 3, round down and subtract 2 """
    fuel = (mass // 3) - 2
    return fuel

def total_fuel(filename):
    with open(filename, 'r') as f:
        sum_of_fuel = 0
        for line in f:
            sum_of_fuel += int(module_fuel(int(line)))
        return sum_of_fuel

real_result = total_fuel('day1_1.txt')
print(real_result)
