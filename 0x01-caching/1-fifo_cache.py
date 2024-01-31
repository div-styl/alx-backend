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

    def first_key(self, dict):
        """return first key"""
        mlist = [i for i in self.cache_data.keys()]
        return mlist[0]
    def put(self, key, item):
        """put"""
        if key is None or item is None:
            return
        if key is not None or item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.cache_data.get(key) is not None:
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                else:
                    discard = self.first_key(self.cache_data)
                    del self.cache_data[self.first_key(self.cache_data)]
                    print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            return self.cache_data


    def get(self, key):
        """get"""
        if key is not None or key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
