# Least Recently Used item will be removed and a new item created:
# Logic: rarely accessed items will be less likely to be used than recently accessed items
#
#
# LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict

class LRUCache:

	def __init__(self, capacity: int):
		self.cache = OrderedDict()
		self.size = capacity


	def get(self, key: int) -> int:
		if key not in self.cache:
			return -1
		else:
			# make the most recent
			self.cache.move_to_end(key)
		return self.cache[key]

	def put(self, key: int, value: int) -> None:
		self.cache[key] = value
		self.cache.move_to_end(key)
		if len(self.cache) > self.size:
			self.cache.popitem(last=False)

	def print(self):
		for key, value in self.cache.items():
			print(f"{key}: {value}")

test = LRUCache(2)
test.put(1,1)
test.put(2,2)
print(test.get(1))
print("before put 3")
test.print()
test.put(3,3)
print("after put 3")
test.print()
print("__________")
print(test.get(2))
test.put(4,4)
print(test.get(1))
print(test.get(3))
print(test.get(4))
