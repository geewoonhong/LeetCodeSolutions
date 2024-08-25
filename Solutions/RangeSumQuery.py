from typing import List

class NumArray:

# 	def __init__(self, nums: List[int]):
# 		self.array = nums

# 	def sumRange(self, left: int, right: int) -> int:
# 		if (right > left) or (left < 0 and right >= len(self.array)):
# 			return None
# 		sum = 0
# 		while left <= right:
# 			sum = sum + self.array[left]
# 			left+=1
# 		return sum

# now lets use the prefix sum array to get the answer in constant time
	def __init__(self, nums: List[int]):
		self.pf = nums
		self.pf[0] = nums[0]
		for i in range(1, len(nums)):
			self.pf[i] = self.pf[i-1] + nums[i]

	def sumRange(self, left: int, right: int) -> int:
		if left == 0:
			return self.pf[right]
		return self.pf[right] - self.pf[left - 1]
