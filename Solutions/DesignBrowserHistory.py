class Node():
    def __init__(self, val=str):
        self.val = val
        self.previous = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str): #init the homepage as a node as the head and tail and set cur ptr
        self.head = self.tail = self.cur = Node(homepage)

    def visit(self, url: str) -> None: #same as add at tail plus update self.cur
        new_node = Node(url)
        new_node.previous = self.cur
        self.cur.next = new_node
        self.cur = new_node
        self.tail = new_node

    def back(self, steps: int) -> str: # need to keep track of where you are in the list
        if steps is None or steps < 0:
            return
        count = 0
        while self.cur is not None:
            if count == steps:
                return self.cur.val
            self.cur = self.cur.previous
            count += 1
        if self.cur == None: #if go back more steps than whats in history, return home
            self.cur = self.head
            return self.head.val

    def forward(self, steps: int) -> str: # need to keep track of where you are in the list
        #whenever you move forwards and hit tail update cur to = tail
        if steps is None or steps < 0:
            return
        count = 0
        while self.cur is not None:
            if count == steps :
                return self.cur.val
            self.cur = self.cur.next
            count += 1
        if self.cur == None: #if go back more steps than whats in history, return home
            self.cur = self.tail
            return self.tail.val

bh = BrowserHistory("homepage.com")
bh.visit("page1.com")
bh.visit("page2.com")										# cur
						#    homepage.com <-> page1.com <-> page2.com
print(bh.back(1)) 		# output: page1.com
print(bh.back(1)) 		# output: homepage.com
print(bh.forward(1)) 	# output: page1.com
												# cur
						#    homepage.com <-> page1.com <-> page2.com
bh.visit("page3.com")
															# cur
						#    homepage.com <-> page1.com <-> page3.com
print(bh.forward(1))
print(bh.back(2))
