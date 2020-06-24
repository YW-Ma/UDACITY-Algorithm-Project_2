# SOLUTION
from collections import OrderedDict
class LRU_Cache(OrderedDict):

    def __init__(self, capacity):
        # Initialize class variables
        # 1. Use OrderedDict to realize a hash map.
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        # 1. Realize cache hit & cache miss
        if key not in self:
            return -1
        # 2. [move_to_end] an item, when it is used.
        self.move_to_end(key)
        return self[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        # 1. Use move_to_end method, when set an item
        self[key] = value
        self.move_to_end(key)
        # 2. Pop the Least recent use item if the number of items exceed the capacity
        if len(self) > self.capacity:
            self.popitem(last = False)

# TEST - 1
print("test case 1")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
#status: [1,2,3,4]

print(our_cache.get(1))       # returns 1
#status: [2,3,4,1]
print(our_cache.get(2))       # returns 2
#status: [3,4,1,2]
print(our_cache.get(5))      # returns -1 (because 5 is not present in the cache)

our_cache.set(5, 5) 
#status: [4,1,2,5]
our_cache.set(6, 6)
#status: [1,2,5,6]

print(our_cache.get(1))      # returns -1 (because the cache reached it's capacity and 1 was the least recently used entry)
#status: [1,2,5,6]
print(our_cache.get(2))      # returns 2
#status: [1,5,6,2]
print(our_cache.get(5))      # returns 5
#status: [1,6,2,5]

# TEST - 2
print("test case 2")
our_cache = LRU_Cache(0)

our_cache.set(1, 1)
our_cache.set(2, 2)
#status: []

print(our_cache.get(1))       # returns -1
#status: []

# TEST - 3
print("test case 3")
our_cache = LRU_Cache(1)

our_cache.set(1, 1)
our_cache.set(2, 2)
#status: [2]

print(our_cache.get(2))       # returns 2
#status: [2]