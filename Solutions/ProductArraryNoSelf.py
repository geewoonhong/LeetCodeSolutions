from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        self.ans = [0] * length
        self.rl = [0] * length
        self.lr = [0] * length
        self.lr[0] = nums[0]
        self.rl[length-1] = nums[length-1]
        for i in range(1, length):
            self.lr[i] = self.lr[i-1] * nums[i]
            self.rl[length-i-1] = self.rl[length-i] * nums[length-i-1]
        for i in range(length):
            if i is 0:
                self.ans[i]=1*self.rl[i+1]
            elif i is (length-1):
                self.ans[i]=self.lr[i-1] * 1
            else:
                self.ans[i] = self.lr[i-1] * self.rl[i+1]
        return self.ans


#improved is to do it one go
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length
        suffProduct = 1
        preProduct = 1
        for i in range(length):
            ans[i] = suffProduct
            suffProduct = suffProduct * nums[i]
        i = length-1
        while i >= 0:
            ans[i] = ans[i] * preProduct
            preProduct = preProduct * nums[i]
            i-=1
        return ans
