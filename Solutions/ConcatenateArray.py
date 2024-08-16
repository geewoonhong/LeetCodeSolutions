# Given an integer array nums of length n,
# you want to create an array ans of length 2n
# where ans[i] == nums[i] and ans[i + n] == nums[i]
# for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.
#

# Return the array ans.


class Solution:
	def getConcatenation(self, nums: list[int]) -> list[int]:
		length = len(nums) * 2
		cpylen = len(nums)
		ans = [0] * length
		i = 0
		cpy = cpylen

		while i < cpylen:
			ans[i] = nums[i]
			ans[cpy + i] = nums[i]
			i+=1
		return ans

sol = Solution()
tst1 = sol.getConcatenation([1,2,1])
tst2 = sol.getConcatenation([1,3,2,1])
print(tst1)
print(tst2)
