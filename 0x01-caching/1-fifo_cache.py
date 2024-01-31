#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """class fifo"""
    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """put"""
        if key and item and self.get(key) != item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lkey = next(iter(self.cache_data))
                self.cache_data.pop(lkey)
                print("DISCARD:", key)

    def get(self, key):
        """get"""
        return self.cache_data.get(key, None)
