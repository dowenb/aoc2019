#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from assertpy import assert_that
from day1_1 import module_fuel, total_fuel

""" Tests: Day one, challenge one for dowenb's attempt at the Advent of Code 2019 Challenge
https://adventofcode.com/2019/day/1
"""

def test_example_module_fuel_loads():
    assert_that(module_fuel(12)).is_equal_to(2)
    assert_that(module_fuel(14)).is_equal_to(2)
    assert_that(module_fuel(1969)).is_equal_to(654)
    assert_that(module_fuel(100756)).is_equal_to(33583)

def test_example_sum_of_fuel():
    example_result = int(total_fuel('day1_1_testdata.txt'))
    assert_that(example_result).is_equal_to(34241)
