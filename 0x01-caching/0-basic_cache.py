#!/usr/bin/env python3
''' 0-basic_cache '''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache '''
    def put(self, key, item):
        ''' implement put method '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' implement get method '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
