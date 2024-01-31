#!/usr/bin/env pthon3
''' LRU Caching '''

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache """
    def __init__(self):
        ''' constructor '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' implement put method '''
        data = self.cache_data

        if key is None or item is None:
            return

        if key not in data:
            if len(data) + 1 > self.MAX_ITEMS:
                l_key, _ = data.popitem(True)
                print("DISCARD:", l_key)

            data[key] = item
            data.move_to_end(key, last=False)
        else:
            data[key] = item

    def get(self, key):
        ''' implement get method '''
        data = self.cache_data

        if key is None or key not in data:
            return None

        if key is not None and key in data:
            data.move_to_end(key, last=False)

        return data[key]
