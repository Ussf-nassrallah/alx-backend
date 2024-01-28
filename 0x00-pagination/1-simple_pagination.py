#!/usr/bin/env python3
'''
1. Simple pagination
'''

from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' index_range: helper function '''
    start_idx: int = (page - 1) * page_size
    end_idx: int = start_idx + page_size

    return (start_idx, end_idx)


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
        ''' Implement get_page method '''
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        (start_idx, end_idx) = index_range(page, page_size)

        data = self.dataset()
        data_len = len(data)

        if start_idx > data_len:
            return []
        else:
            return data[start_idx:end_idx]
