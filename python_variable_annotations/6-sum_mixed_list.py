#!/usr/bin/env python3
"""
Task 6.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    float sum of mixed list of ints and floats
    """
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
