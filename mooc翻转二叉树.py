from collections import deque


class BinaryTree():
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

    def getVal(self):
        return self.key

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, subTree):
        self.left = subTree

    def setRight(self, subTree):
        self.right = subTree


def seq2tree(seq):
    mydeque = deque()
    root = BinaryTree(seq.pop(0))
    mydeque.append(root)
    while len(seq) > 1:
        if seq[0] != None and seq[1] != None:
            left = BinaryTree(seq.pop(0))
            right = BinaryTree(seq.pop(0))
            mydeque.append(left)
            mydeque.append(right)

            node = mydeque.popleft()
            node.setLeft(left)
            node.setRight(right)
        elif seq[0] != None and seq[1] == None:
            left = BinaryTree(seq.pop(0))
            seq.pop(0)
            mydeque.append(left)
            mydeque.popleft().setLeft(left)
        elif seq[0] == None and seq[1] != None:
            seq.pop(0)
            right = BinaryTree(seq.pop(0))
            mydeque.append(right)
            mydeque.popleft().setRight(right)
        elif seq[0] == None and seq[1] == None:
            seq.pop(0)
            seq.pop(0)
            mydeque.popleft()
    if len(seq) != 0:
        leftone = BinaryTree(seq[0])
        mydeque.popleft().setLeft(leftone)
    return root


#, root.getRight().key


def reverseTree(root):
    if root == None:
        return None
    else:
        k = root.getLeft()
        root.setLeft(root.getRight())
        root.setRight(k)
        reverseTree(root.getLeft())
        reverseTree(root.getRight())


def inorderTree(root, res):
    if root == None:
        return None
    else:
        inorderTree(root.getLeft(), res)
        res.append(root.getVal())
        inorderTree(root.getRight(), res)
    return res


lst = input().split()
tree = seq2tree(lst)
reverseTree(tree)
inorder = inorderTree(tree, [])
print(' '.join(map(str, inorder)))  # 请自行确定打印方式