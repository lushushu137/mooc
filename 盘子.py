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


rightlist = '0123456789'
test = '4230178956'
testlist = list(test)
mystack = Stack()
# print(testlist)
i = 0
while i < len(rightlist):
    mystack.push(rightlist[i])
    print('加进去的：', mystack.show())
    while mystack.IsEmpty() is False and testlist[0] == mystack.peek():
        mystack.pop()
        print('拿掉盘子后剩下的：', mystack.show())
        testlist.pop(0)
        print('拿盘子的顺序：', testlist)
    i += 1
    print(i)
# print(mystack.show())
if testlist == []:
    print('Yes')
else:
    print('No')
