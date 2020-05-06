test = 'beepooxxxyz'


class Stack():
    def __init__(self):
        self.item = []

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def push(self, n):
        return self.item.append(n)

    def size(self):
        return len(self.item)

    def IsEmpty(self):
        return self.item == []

    def show(self):
        return self.item


mystack = Stack()
test_list = list(test)

for i in test_list:
    if mystack.IsEmpty():
        mystack.push(i)
    elif mystack.peek() == i:
        mystack.pop()
    else:
        mystack.push(i)

if mystack.IsEmpty():
    print(None)
else:
    print(''.join(mystack.show()))