#!/usr/bin/python3
"""
class LFUCache inheriting from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a LFU caching system
    """

    def __init__(self):
        """
        initialization method for the class
        """
        self.queue = []
        self.lfu = {}
        super().__init__()

    def put(self, key, item):
        """
        method used to add or update entries in the data structure,
        making it accessible for later use
        """
        if key and item:
            if (len(self.queue) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                delete = self.queue.pop(0)
                self.lfu.pop(delete)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

            if self.cache_data.get(key):
                self.queue.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0

            insert_index = 0
            while (insert_index < len(self.queue) and
                   not self.lfu[self.queue[insert_index]]):
                insert_index += 1
            self.queue.insert(insert_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """
        For retrieval of a value associated with a specific "key"
        within an object
        """
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.queue.index(key) + 1 != len(self.queue):
                while (self.queue.index(key) + 1 < len(self.queue) and
                       self.lfu[key] >=
                       self.lfu[self.queue[self.queue.index(key) + 1]]):
                    self.queue.insert(self.queue.index(key) + 1,
                                      self.queue.pop(self.queue.index(key)))
        return self.cache_data.get(key)
