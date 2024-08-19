#!/usr/bin/env python3
'''using lifo in this code'''


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO class desc'''

    def __init__(self):
        '''Init function for inh'''
        super().__init__()

    def put(self, key, item):
        '''Put function self item'''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item

    def get(self, key):
        '''finally get func'''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
