class Node():
    def __init__(self, inivalue):
        self.value = inivalue
        self.next = None

    def getdata(self):
        return self.value

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.value = newdata

    def setnext(self, newnext):
        self.next = newnext


class Queue():
    def __init__(self):
        self.head = None

    def __str__(self):
        newstr = ''
        curr = self.head
        while curr != None:
            newstr += str(curr.getdata())
            curr = curr.getnext()
        return newstr

    def pop(self):  #移除队列底端元素（最右边节点),并返回该元素
        curr = self.head
        previous = Node(0)
        while curr.getnext() != None:
            previous = curr
            curr = curr.getnext()
        previous.setnext(None)
        return curr.getdata()

    def add(self, newnode):  #添加元素到队列顶部（最左边节点）
        newnode = Node(newnode)
        newnode.setnext(self.head)
        self.head = newnode
        # print(self.head)

    def size(self):
        # print(self.head)
        curr = self.head
        i = 0
        # print(curr)
        while curr != None:
            curr = curr.getnext()
            i += 1
        return i

    def IsEmpty(self):
        return self.head == None

    def show(self):
        return self.head


def func(S):
    newstr = Queue()
    l = list(S)
    l.reverse()
    for i in l:
        newstr.add(i)

    output = str(newstr)
    # print('debug:', output)

    move_times = 0
    while move_times < newstr.size():
        newstr.add(newstr.pop())
        # print(newstr.size())
        # print(str(newstr))
        # print('output:', output)
        if str(newstr) < output:
            output = str(newstr)
            # print('output:', output)
        move_times += 1
    return output


S = 'cba'  #eval(input())
print('结果:', func(S))
