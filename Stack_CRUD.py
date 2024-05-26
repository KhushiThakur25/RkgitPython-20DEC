class Stack:
    def __init__(self):
        self.li = []
    def push(self,data):
        self.li.append(data)
    def pop(self):
        self.li.pop()
    def peek(self):
        return self.li[len(self.li)-1]

obj = Stack()
obj.push(40)
obj.push(30)
obj.push(20)
obj.push(10)
obj.push(5)
obj.pop()
print(obj.peek())

