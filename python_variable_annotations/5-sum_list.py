#!/usr/bin/env python3
"""
Task 5.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    return sum of values in input_list
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
