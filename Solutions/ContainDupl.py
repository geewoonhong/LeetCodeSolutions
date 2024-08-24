from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stack = []
        for i in nums:
            if i in stack and stack is not None:
                return True
            stack.append(i)
        return False


#faster
#the method set() uses a hash table where each immutable element in the table
# has a hash number which is used to immediately lookup its corresponding value
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #set up a hash table
        seen = set()
        for i in nums:
            #if the current element in nums has a same hash value in seen
            # then that means there is a duplicate
            if i in seen and seen is not None:
                return True
            #if no dupls exist then add a new hash key and its value being i
            # i being the current element in nums
            seen.add(i)
        return False
