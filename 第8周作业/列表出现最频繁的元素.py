def myfunc(alist, k):
    # if len(alist) < k:
    #     return ' '.join(map(str, alist))
    myDict = {}
    for x in alist:
        myDict[x] = myDict.get(x, 0) + 1

    sortedTuple = sorted(myDict.items(), key=lambda a: (-a[1], a[0]))
    result = [j[0] for j in sortedTuple[:k]]
    print(*result)


alist = eval(input())
k = int(input())
myfunc(alist, k)