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
        return print(self.item)


mystack = Stack()


def rightbracket(bracketinput):
    def make_bracketlist(bracketinput):
        bracketlist = []
        for i in bracketinput:
            bracketlist.append(i)
        return bracketlist

    mybracketlist = make_bracketlist(bracketinput)
    pair_dict = {'(': ')', '[': ']', '{': '}'}

    for i in mybracketlist:
        if i in '([{':
            mystack.push(i)
        else:
            if pair_dict[mystack.peek()] == i:
                mystack.pop()
            else:
                break
    mystack.show()
    if mystack.IsEmpty():
        return True
    else:
        return False


print(rightbracket("()(){{]"))