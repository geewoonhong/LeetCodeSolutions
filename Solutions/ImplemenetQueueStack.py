class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(len(self.stack)-1)

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def empty(self) -> bool:
        count = 0
        for int in self.stack :
            count+=1
        if count == 0 :
            return True
        else:
            False
