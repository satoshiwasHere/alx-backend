#!/usr/bin/python3
"""
class MRUCache inheriting from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    'MRUCache' defines a MRU cache caching system
    """

    def __init__(self):
        """
        initialization method for the class
        """
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """
        method used to add or update entries in the data structure,
        making it accessible for later use
        """
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        For retrieval of a value associated with a specific "key"
        within an object
        """
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
