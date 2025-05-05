#!/usr/bin/env python3
"""
Task 8.
"""
from typing import Callable
import random


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
