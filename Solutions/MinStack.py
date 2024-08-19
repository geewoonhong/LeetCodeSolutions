# custom stack
# push, pop, top, retrieve min in constant Time O(1) time
# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# class MinStack:
# 	def __init__(self):
# 		self.stack = []

# 	def push(self, val: int) -> None:
# 		self.stack.append(val)

# 	def pop(self) -> None:
# 		if self.stack:
# 			self.stack.pop()

# 	def top(self) -> int:
# 		if self.stack:
# 			return self.stack[len(self.length) - 1]
# 		return None

# 	def getMin(self) -> int:
# 		if self.stack:
# 			return min(self.stack)
# 		return None

# refined way using something like a matrix to constantly update and store
# the min_ele
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        Min_val= self.getMin()
        if Min_val == None or val < Min_val:
            Min_val = val
        self.stack.append([val, Min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[len(self.stack) - 1][0]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
