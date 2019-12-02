import math

""" Day one, challenge one for dowenb's attempt at the Advent of Code 2019 Challenge
https://adventofcode.com/2019/day/1
"""

def module_fuel(mass):
    """ Take mass, divide by 3, round down and subtract 2 """
    fuel = math.floor(int(mass / 3))
    return (fuel - 2)

print(module_fuel(12))
