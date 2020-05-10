from collections import deque


class binTree():
    def __init__(self, val):
        self.key = val
        self.children = []
        self.childrenNum = -1

    def addChild(self):
        self.childrenNum += 1
        # print(self.childrenNum)
        self.children.append(binTree(0))

    def setVal(self, val):
        self.key = val

    def getChildren(self):
        return self.children[self.childrenNum]


def makeTree(listTree):
    mystack = deque()
    currNode = binTree(0)
    for i in listTree:
        # print(i)
        # print(currNode.key, currNode.children)
        if i == '[':
            mystack.append(currNode)
            currNode.addChild()
            currNode = currNode.getChildren()

        elif i == ']':
            currNode = mystack.pop()
        elif i in ', ':
            continue
        else:
            if currNode.key == 0:
                currNode.setVal(i)
            else:
                currNode.setVal(str(currNode.key) + str(i))
            # print(currNode.key)
    currNode = currNode.children[0]
    return currNode


def backOrder(root, mylist):
    if root == None:
        return None
    else:
        for i in range(len(root.children)):
            backOrder(root.children[i], mylist)
        mylist.append(root.key)
    return mylist


tree = makeTree(str(input()))
mylist = backOrder(tree, [])

print(' '.join(mylist))
