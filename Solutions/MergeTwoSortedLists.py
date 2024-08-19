from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         #set the two heads
#         min1 = list1
#         min2 = list2
#         if list1 is None and list2 is None:
#             return None
#         if list1 is None and list2 is not None:
#             return list2
#         if list1 is not None and list2 is None:
#             return list1


#         if min1.val < min2.val:
#             cur = min1
#             cur.val =min1.val
#             head = cur
#             min1 = min1.next
#         else :
#             cur = min2
#             cur.val = min2.val
#             head = cur
#             min2 = min2.next
#         while cur is not None :
#             if min1.val < min2.val :
#                 cur.val = min1.val
#                 min1 = min1.next
#                 cur = cur.next
#             else :
#                 cur.val = min2.val
#                 min2 = min2.next
#                 cur = cur.next
#         return head

# revised and updated
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #set a dummy node to start
        cur = res = ListNode()

        if list1 is None and list2 is None:
            return None
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1 #move the ptr next to list1
                cur = list1 #move cur to list1
                list1 = list1.next #iterate through list1
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next #iterate through list2

        if list1 is not None or list2 is not None: #if there are remaining nodes in either
            cur.next = list1 if list1 is not None else list2 #set the next ptr of cur to which ever list's remaining nodes
        return res.next



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

sol = Solution()
merged_head = sol.mergeTwoLists(node1, node4)

# Print reverse
cur = merged_head
while cur is not None:
    if cur.next is None:
        print(cur.val)
        break
    print(cur.val, end =" -> ")
    cur = cur.next
