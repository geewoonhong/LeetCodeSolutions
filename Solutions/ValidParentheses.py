# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.()
# Open brackets must be closed in the correct order. {()} not ( { ) }
# Every close bracket has a corresponding open bracket of the same type.  not (}

# the following solution runs into a lot of issues when dealing with edge cases
# class Solution:
# 	def isValid(self, s: str) -> bool:
# 		length = len(s)
# 		T_flag = 0
# 		left, right = 0, length - 1
# 		if length % 2 != 0 :
# 			return False
# 		if s[0] == ")" or s[0] == "}" or s[0] == "]":
# 			return False
# 		while left < right:
# 			if s[left] == "(":
# 				while right > left:
# 					if s[right] == ")" and (s[right-1] != "{" and s[right-1] != "["):
# 						T_flag = 1 #mark true flag
# 						break
# 					right-=1
# 				if T_flag == 0: # if you dont find the closing para flag is false
# 					return False
# 			elif s[left] == "{":
# 				while right > left:
# 					if s[right] == "}" and (s[right-1] != "(" and s[right-1] != "["):
# 						T_flag = 1 #mark true flag
# 						break
# 					right-=1
# 				if T_flag == 0: # if you dont find the closing para flag is false
# 					return False
# 			elif s[left] == "[":
# 				while right > left:
# 					if s[right] == "]" and (s[right-1] != "{" and s[right-1] != "("):
# 						T_flag = 1 #mark true flag
# 						break
# 					right-=1
# 				if T_flag == 0: # if you dont find the closing para flag is false
# 					return False
# 			left += 1
# 			right = length - 1
# 			T_flag = 0
# 		return True

# the trick is to use a stack data structure
class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		mapping = {")": "(", "}": "{", "]": "["}

		for char in s:
			if char in mapping:
				# top_element = stack.pop() if stack else '#' #ternary operator
				if stack:
					top_element = stack.pop()
				else :
					top_element = '#'
				if mapping[char] != top_element:
					return False
			else:
				stack.append(char)
		return not stack # asks if the stack is empty. If it is then the method returns true.


sol = Solution()
tst1 = sol.isValid("()")
tst2 = sol.isValid("()[]{}")
tst3 = sol.isValid("(]")
tst4 = sol.isValid("{()}")
tst5 = sol.isValid("([)]")
print(tst1)
print(tst2)
print(tst3)
print(tst4)
print(tst5)
