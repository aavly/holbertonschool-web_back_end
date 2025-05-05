#!/usr/bin/env python3
"""
Task 9.
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate this function's parameters and return
    values with the appropriate values
    """
    return [(i, len(i)) for i in lst]
