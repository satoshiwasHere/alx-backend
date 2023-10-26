#!/usr/bin/python3
"""
A class 'BasicCache' inheriting from 'BaseCaching' and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    """

    def put(self, key, item):
        """
        Assign the item to the dictionary and
        stores a key value pair
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key
        """
        return self.cache_data.get(key)
