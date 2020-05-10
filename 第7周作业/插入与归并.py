def whichSort(alist, blist):
    for i in range(len(blist) - 1):
        if blist[:i + 1] == sorted(blist[:i + 1]):
            continue
        else:
            if blist[i:] == alist[i:]:
                return ('Insertion Sort', i)
            else:
                return ('Merge Sort', i)


def nextRes(alist, blist):
    if whichSort(alist, blist)[0] == 'Merge Sort':
        print('Merge Sort')
        print(nextMerge(alist, blist))
    else:
        print('Insertion Sort')
        print(nextInsertion(alist, blist, whichSort(alist, blist)[1]))


def nextInsertion(alist, blist, i):
    for j in range(len(blist[:i])):
        if blist[i] > blist[j] and blist[i] < blist[j + 1]:
            blist.insert(j + 1, blist[i])
            blist.pop(i + 1)
            return ' '.join(blist)


def nextMerge(alist, blist):
    subleng = 2
    res = alist

    def doIt(theList, theLength):
        sublist = [
            sorted(theList[i:i + theLength])
            for i in range(0, len(theList), theLength)
        ]
        nextRes = []
        for ls in sublist:
            nextRes += ls
        return nextRes

    while res != blist:
        res = doIt(res, subleng)
        subleng = subleng * 2
    res = doIt(res, subleng)
    return ' '.join(res)


# 3 1 2 8 7 5 9 4 0 6 // 1 2 3 8 4 5 7 9 0 6

alist = input().split()
blist = input().split()
nextRes(alist, blist)
