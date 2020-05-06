


def mergesort_onestep(alist):
    def merge(l1, l2):
        mylist = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                mylist.append(l1[i])
                i += 1
            else:
                mylist.append(l2[j])
                j += 1

        if i <= len(l1):
            mylist += l1[i:]
        if j <= len(l2):
            mylist += l2[j:]
        return mylist

    if len(alist) == 1:
        return alist
    else:
        midpoint = len(alist) // 2
        left = alist[:midpoint]
        right = alist[midpoint:]
        return merge(mergesort(left), mergesort(right))


def insertionsort(alist):
    k = 1
    while k in range(len(alist)):
        j = 0
        while j in range(k):
            if alist[k] > alist[j]:
                j += 1
            else:
                val = alist.pop(k)
                alist.insert(j, val)
                break
        k += 1
    return alist


def issequence(alist):
    flag = True
    for i in range(len(alist) - 1):
        if flag:
            if alist[i + 1] >= alist[i]:
                continue
            else:
                flag = False
        else:
            break
    return flag


def isinsertionsort(alist, newlist):
    flag = 'Insertion Sort'
    for k in range(len(newlist)):
        if issequence(newlist[:k]) and newlist[k:] == alist[k:]:
            for j in range(len(newlist[:(k + 1)])):
                if newlist[k] < newlist[j]:
                    val = newlist.pop(k)
                    newlist.insert(j, val)
                    return flag, newlist
                else:
                    continue
        else:
            continue
    flag = 'Merge Sort'
    
    mergesort_onestep(newlist)
    return flag


a = input().split()
a1 = list(map(eval, a))
b = input().split()
b1 = list(map(eval, b))

print(isinsertionsort(a1, b1))