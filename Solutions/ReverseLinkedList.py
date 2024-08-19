#the import Optional     makes it explicit in the function signature
# that a return value can be None
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find the tail
        cur = head
        count = 0
        val = []
        while cur != None:
            val.append(cur.val)
            cur = cur.next
            count += 1 #count would be 5 in case 1
        # head = cur # this is wrong
        cur = head
        while cur != None :
            cur.val = val[count-1]
            cur = cur.next
            count -= 1
        cur = None
        return head

# cur is not None: checks the existence of the cur object itself.
# cur.next != None: checks the existence of the next node
# cur in the list.

# Context:
# cur is not None: ensure that cur (the current node) is valid
# cur.next != None: determine if there is a next node available
# (going through linked list)



#tests
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
reversed_head = sol.reverseList(node1)

# Print reverse
cur = reversed_head
while cur is not None:
    if cur.next is None:
        print(cur.val)
        break
    print(cur.val, end =" -> ")
    cur = cur.next
