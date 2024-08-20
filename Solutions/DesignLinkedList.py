class Node:
	def __init__(self, val):
		self.val = val
		self.previous = None
		self.next = None

class MyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def get(self, index: int) -> int:
		if index is None or self.head is None:
			return -1
		count = 0
		cur = self.head
		while cur is not None:
			if count == index:
				return cur.val
			else:
				cur = cur.next
				count += 1
		return -1 #index out of bounds

	def addAtHead(self, val: int) -> None:
		new_node = Node(val)
		if self.head is None : #if no head or tail the new node is both head and tail
			self.head = self.tail = new_node
		else :
			new_node.next = self.head
			self.head.previous = new_node
			self.head = new_node
		return

	def addAtTail(self, val: int) -> None:
		new_node = Node(val)
		if self.tail is None:
			self.tail = self.head = new_node
		else :
			new_node.previous = self.tail
			self.tail.next = new_node
			self.tail = new_node
		return

	def addAtIndex(self, index: int, val: int) -> None:
		if index is None or index < 0:
			return
		new_node = Node(val)
		if index == 0: #same as inserting in head
			if self.head is None:
				self.head=self.tail=new_node
			else:
				new_node.next = self.head
				self.head.previous = new_node
				self.head = new_node
			return
		count = 0
		cur = self.head
		while cur is not None:
			if count == index :
				new_node.next = cur
				new_node.previous = cur.previous
				cur.previous.next = new_node
				cur.previous = new_node
				return
			cur = cur.next
			count += 1
		if cur is None and count == index:
			new_node.previous = self.tail
			self.tail.next = new_node
			self.tail = new_node
		return

	def deleteAtIndex(self, index: int) -> None:
		if index is None or index < 0:
			return
		if self.head is None:
			return
		if index == 0: #same as inserting in head
			if self.head.next is None: #only one node left
				self.head = self.tail = None
			else:
				self.head = self.head.next
				self.head.previous = None
			return

		count = 0
		cur = self.head
		while cur is not None:
			if count == index:
				if cur.next is None:
					cur.previous.next = None
					self.tail = cur.previous
				else:
					cur.previous.next = cur.next
					cur.next.previous = cur.previous
				return
			cur = cur.next
			count += 1
		return

dll = MyLinkedList()
dll.addAtHead(1)
dll.addAtTail(2)
dll.addAtTail(3)
dll.deleteAtIndex(1)
print(dll.get(0))  # Output: 1
print(dll.get(1))  # Output: 3

dll.deleteAtIndex(0)
print(dll.get(0))  # Output: 3

dll.deleteAtIndex(0)
print(dll.get(0))  # Output: -1 (list is now empty)
