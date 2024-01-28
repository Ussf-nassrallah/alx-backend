#!/usr/bin/env python3
'''
0. Simple helper function
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' index_range: helper function '''
    start_idx: int = (page - 1) * page_size
    end_idx: int = start_idx * page_size

    return (start_idx, end_idx)
