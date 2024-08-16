# class name:
# 	def methodName1(self, parameters):

# 	def methodName2(self, Parameters):

# python must use consistent spaces or indents dont mix the two

# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
# square first then sort

#first try: using bubble sort time: O(n^2)
# class Solution:
# 	def sortedSquares(self, nums: list[int]) -> list[int]: #return should also be a list[int]
# 		i = 0
# 		length = len(nums)
# 		while i<length:
# 			nums[i] = nums[i]*nums[i]
# 			i+=1
# 		i=0
# 		j=0
# 		box=0
# 		while i < length:
# 			while j < length - 1:
# 				if nums[j] > nums[j+1]:
# 					box = nums[j+1]
# 					nums[j+1] = nums[j]
# 					nums[j] = box
# 				j+=1
# 			j=0
# 			i+=1
# 		return nums

#2nd try
class Solution:
	def sortedSquares(self, nums: list[int]) -> list[int]:
		length = len(nums)
		res = [0] * length
		left, right = 0, length - 1
		index = length - 1

		while left <= right:
			leftSq = nums[left] * nums[left]
			rightSq = nums[right] * nums[right]
			if leftSq > rightSq :
				res[index] = leftSq
				left+=1
			else :
				res[index] = rightSq
				right-=1
			index-=1
		return res


sol = Solution()  # instance of the Solution class
result = sol.sortedSquares([-4, -1, 0, 3, 10])  # Call method
print(result)
