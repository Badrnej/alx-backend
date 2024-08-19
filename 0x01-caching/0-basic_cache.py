#!/usr/bin/env python3
'''a class BasicCache that inherits from
BaseCaching and is a caching system'''


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    '''class BasicCache that inherits from
    BaseCaching and is a caching system'''
    def __init__(self):
        """iit file"""
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''get fuction'''
        if key not in self.cache_data.keys() or key is None:
            return None
        return self.cache_data.get(key)
