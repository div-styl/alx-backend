#!/usr/bin/env python3
"""
create a class BasicCache that inherits
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class of basic cache"""

    def __init__(self):
        """return super"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None or key in self.cache_data:
            return self.cache_data.get(key)
        return None
