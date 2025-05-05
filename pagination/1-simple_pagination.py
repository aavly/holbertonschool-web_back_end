#!/usr/bin/env python3
"""
Task 0. Write a function that takes two integer
arguments and returns a tuple (size 2) containing a
start index and an end index corresponding to the range
of indexes.
"""
import csv
from typing import List, Tuple


def index_range(page, page_size):
    """
    Returns a tuple (size 2) containing a start index
    and an end index corresponding to the range of indexes.
    """
    start_index = (page-1) * page_size
    end_index = page_size + start_index
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the correct page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start:end] if start < len(dataset) else []
