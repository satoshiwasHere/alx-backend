#!/usr/bin/python3
"""
class FIFOCache inheriting from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    'FIFOCache' defines a FIFO caching system
    """

    def __init__(self):
        """
        initialization method for the class
        """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """
        The method used to add or update entries in the data structure,
        making it accessible for later use
        """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """
        For retrieval of a value associated with a specific "key"
        within an object
        """
        return self.cache_data.get(key)
