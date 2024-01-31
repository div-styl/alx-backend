#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits
"""


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """class fifo"""

    def __init__(self):
        """init"""
        super().__init__()
        self.last = 0

    def put(self, key, item):
        """adds an item to cache"""
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.last)
                    print('DISCARD:', self.last)
                self.last = key

    def get(self, key):
        """return and item from the cache"""
        return self.cache_data.get(key, None)
