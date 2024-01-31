#!/usr/bin/env pthon3
''' 1. FIFO caching '''

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache """
    def __init__(self):
        ''' constructor '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' implement put method '''
        data = self.cache_data
        if key is None or item is None:
            return
        data[key] = item

        if len(data) > BaseCaching.MAX_ITEMS:
            f_key, _ = data.popitem(False)
            print("DISCARD:", f_key)

    def get(self, key):
        ''' implement get method '''
        data = self.cache_data
        if key is None or key not in data:
            return None
        return data[key]
