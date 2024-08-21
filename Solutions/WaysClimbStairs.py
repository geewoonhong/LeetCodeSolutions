class Solution:
	def climbstairs(self, n: int) -> int:
		if n == 1:
			return 1
		if n == 2:
			return 2
		return self.climbstairs(n - 1) + self.climbstairs(n - 2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one_bef = 1
        two_bef = 1
        total = 0
        for i in range(2, n + 1): # i will be 2, 3, 4, 5 and the loop runs 4 times
            total = one_bef + two_bef
            two_bef = one_bef
            one_bef = total
        return total
