class BST():
    def __init__(self, key, val=0):
        self.key = key
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def addVal(self, val):
        self.val = val

    def setLeftChild(self, subTreeKey):
        self.leftChild = BST(subTreeKey)

    def setRightChild(self, subTreeKey):
        self.rightChild = BST(subTreeKey)

    def __iter__(self):
        if self:
            if self.leftChild != None:
                for elem in self.leftChild:
                    yield elem
            yield self
            if self.rightChild != None:
                for elem in self.rightChild:
                    yield elem


def buildKeyTree(k):
    root = BST(0)
    nodes = [root]
    j = 1
    while j < k:
        nodes[0].setLeftChild(j)
        if j + 1 < k:
            nodes[0].setRightChild(j + 1)
            nodes.append(nodes[0].leftChild)
            nodes.append(nodes[0].rightChild)
        else:
            nodes.append(nodes[0].leftChild)
        nodes.pop(0)
        j += 2
    return root


def addVal(tree, alist):
    for nodes in tree:
        # print(nodes.key, alist[0])
        nodes.val = alist[0]
        alist.pop(0)
    return tree


def layerOrder(root):
    mydeque = [root]
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


alist = sorted([int(i) for i in input().split()])
k = len(alist)
theTree = buildKeyTree(k)
theTree = addVal(theTree, alist)
# print(theTree.val)
print(layerOrder(theTree))