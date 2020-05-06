from collections import deque


class binTree():
    def __init__(self, key, val=None):
        self.key = key
        self.val = None
        self.leftChild = None
        self.rightChild = None

    def setLeftChild(self, subTree):
        self.leftChild = subTree
        # print('左子节点：', self.leftChild.key)

    def setRightChild(self, subTree):
        self.rightChild = subTree
        # print('右子节点：', self.rightChild.key)

    def addVal(self, val):
        self.val = val

    def __iter__(self):
        if self:
            if self.leftChild != None:
                for elem in self.leftChild:
                    yield elem
            yield self
            if self.rightChild != None:
                for elem in self.rightChild:
                    yield elem


def buildKeyTree(inputNum, nodesList):
    keyList = [binTree(i) for i in range(inputNum)]
    # print(inputNum, nodesList, keyList)
    for key in keyList:
        if nodesList[0][0] != -1:
            key.setLeftChild(keyList[nodesList[0][0]])
        if nodesList[0][1] != -1:
            key.setRightChild(keyList[nodesList[0][1]])
        nodesList.popleft()
    return keyList[0]


def addValTree(root, vals):
    for elem in root:
        elem.addVal(vals[0])
        vals.pop(0)


def layerOrder(root):
    mydeque = [root]
    res = []
    while len(mydeque) != 0:
        res.append(mydeque[0].val)
        if mydeque[0].leftChild != None:
            mydeque.append(mydeque[0].leftChild)
        if mydeque[0].rightChild != None:
            mydeque.append(mydeque[0].rightChild)
        mydeque.pop(0)
    return ' '.join([str(i) for i in res])


inputNum = int(input())
nodesList = deque()
k = 0
while k < inputNum:
    nodesList.append([int(j) for j in input().split()])
    k += 1

valList = [int(j) for j in input().split()]

sortedVals = sorted(valList)
root = buildKeyTree(inputNum, nodesList)
# print(root.leftChild.key)
addValTree(root, sortedVals)
print(layerOrder(root))