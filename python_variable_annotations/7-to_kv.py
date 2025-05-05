#!/usr/bin/env python3
"""
Task 7.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    String and int/float to tuple
    """
    sqrd = v*v
    return (k, sqrd)
