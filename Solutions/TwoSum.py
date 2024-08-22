from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		ans = []
		i = 0
		j = 1
		length = len(nums)
		while i < length:
			while j < length:
				if nums[j] == target - nums[i]:
					ans.append(j)
					ans.append(i)
					return ans
				j+=1
			i += 1
			j = i + 1

# lets use a hash table

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		map = {}
		#to add something to the hash map
		# map[key] = value
		i = 0
		length = len(nums)
		#by default starts at 0 to length-1
		for i in range(length):
			#the value is the indices of the location
			map[nums[i]] = i
		for i in range(length):
			x = target - nums[i] #the value that you are looking for
			if x in map and map[x] != i:
				return [i, map[x]]
