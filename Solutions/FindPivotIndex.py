from typing import List

# class Solution:
# 	def pivotIndex(self, nums: List[int]) -> int:
# 		length = len(nums)
# 		self.lrsum = [0] * length
# 		self.rlsum = [0] * length
# 		self.lrsum[0] = nums[0]
# 		self.rlsum[length -1] = nums[length -1]
# 		for i in range(1, length):
# 			self.lrsum[i] = self.lrsum[i-1] + nums[i]
# 			self.rlsum[length-i-1] = self.rlsum[length-i] + nums[length - i -1]
# 		i = 0
# 		j = length - 1
# 		while i < length:
# 			while j > 0:
# 				if i == 0 and self.rlsum[1] == 0:
# 					return 0
# 				if i is not 0  and j is not length -1 and (i == j) and (self.lrsum[i-1]==self.rlsum[j+1]):
# 					return i
# 				j-=1
# 			j = length -1
# 			i+=1
# 		if self.lrsum[length-2] == 0:
# 					return length-1
# 		return -1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)

        # Edge case: empty list
        if length == 0:
            return -1

        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Initialize left sum as 0
        left_sum = 0

        # Iterate over the array
        for i in range(length):
            # Right sum would be the total sum minus left sum and current element this is the KEY
            right_sum = total_sum - left_sum - nums[i]

            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i

            # Update left sum
            left_sum += nums[i]

        # If no pivot index is found, return -1
        return -1

sol = Solution()

nums = [2,1,-1]
tst1 = [1,7,3,6,5,6]
tst2 = [-1,-1,-1,-1,-1,0]
tst3 = [-1,-1,1,1,0,0]
print(sol.pivotIndex(nums))
print(sol.pivotIndex(tst1))
print(sol.pivotIndex(tst2))
print(sol.pivotIndex(tst3))
