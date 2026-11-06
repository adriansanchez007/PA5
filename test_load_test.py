#######################################
# Programmer: Adrian Sanchez
# Class: ENSC-201-01, Fall 2026
# PA5
# 11/5/26
# Description:
# Reference used: PA5 document
#######################################

import numpy as np

from load_test import *


def test_calculate_stress():
    assert calculate_stress(6, 4) == 1.5 # common test case
    assert calculate_stress(0, 576) == 0 # zero force test case
    assert calculate_stress(5.5, 10) == 0.55 # floating value for force test case


def test_classify_stress():
    assert classify_stress(6, 10) == "SAFE" # stress is below 80% of the stress limit
    assert classify_stress(12, 14) == "WARNING" # stress is between 80% and 100% of the limit
    assert classify_stress(10, 5) == "FAILURE" # stress exceeds the stress limit


def test_run_load_test():
    assert run_load_test(80, 12, 4, 57, 100) == 0 # 0 failed cycles
    assert run_load_test(90, 15, 3, 70, 1) == 1 # test failure on cycle 1
    assert run_load_test(90, 15, 5, 70, 2) == 5 # test failure after multiple cycles
    assert run_load_test(80, 0.1, 1, 10, 10) == 0 # edge case where the stress is at 80% of limit