class StackNode:
    def __init__(self, val, prev, min):
        self.val = val
        self.prev = prev
        self.min = min


class MinStack:

    def __init__(self):
        self.head = None
        self.min = None

    def push(self, val: int) -> None:
        node = StackNode(val, self.head, self.min)
        self.min = min(val, self.min) if self.min is not None else val
        self.head = node

    def pop(self) -> None:
        if self.head is not None:
            self.min = self.head.min
            self.head = self.head.prev

    def top(self) -> int:
        # The question never mention about calling top() with nothing in stack, so I ignore it for now
        return self.head.val

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
