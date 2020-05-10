class BST():
    def __init__(self, key=None):
        self.key = key
        self.val = 0
        self.leftChild = None
        self.rightChild = None

    def __iter__(self):
        if self:
            if self.leftChild != None:
                for elem in self.leftChild:
                    yield elem
            # print(self.key)
            yield self
            if self.rightChild != None:
                for elem in self.rightChild:
                    yield elem

    def setVal(self, val):
        self.val = val

    def addNode(self, node):
        if self.key:
            self._put(node, self)
        else:
            self.key = node.key

    def _put(self, node, curr):
        # print(self.key, node.key, curr.key)
        if node.key < curr.key:
            if curr.leftChild == None:
                curr.leftChild = node
            else:
                self._put(node, curr.leftChild)
        else:
            if curr.rightChild == None:
                curr.rightChild = node
            else:
                self._put(node, curr.rightChild)


def buildKeyTree(alist):
    theTree = BST()
    for key in alist:
        theTree.addNode(BST(key))
    return theTree


def sumList(alist):
    res = []
    for i in range(len(alist)):
        res.append(sum(sorted(alist)[i:]))
    return res


def keyValDict(keyList, valList):
    myDict = {}
    for key in range(len(keyList)):
        myDict[sorted(keyList)[key]] = valList[key]
    return myDict


def addVal(keyTree, myDict):

    for node in keyTree:
        # print(node.key, myDict[node.key])
        node.setVal(myDict[node.key])
    return keyTree


def layerOrder(theTree):
    mydeque = [theTree]
    res = []
    while len(mydeque) != 0:
        # print(mydeque[0].val)
        res.append(mydeque[0].val)
        if mydeque[0].leftChild != None:
            mydeque.append(mydeque[0].leftChild)
        if mydeque[0].rightChild != None:
            mydeque.append(mydeque[0].rightChild)
        mydeque.pop(0)
    return ' '.join([str(i) for i in res])


alist = [int(i) for i in input().split()]
theTree = buildKeyTree(alist)
theValList = sumList(alist)
theDict = keyValDict(alist, theValList)
# print(theDict)
theTree = addVal(theTree, theDict)
print(layerOrder(theTree))