#!/usr/bin/env python3
"""
Task 0. Write a function that takes two integer
arguments and returns a tuple (size 2) containing a
start index and an end index corresponding to the range
of indexes.
"""


def index_range(page, page_size):
    """
    Returns a tuple (size 2) containing a start index
    and an end index corresponding to the range of indexes.
    """
    start_index = (page-1) * page_size
    end_index = page_size - start_index
    return (start_index, end_index)
