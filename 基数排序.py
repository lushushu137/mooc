import math

listlist = [[] for _ in range(10)]
# for i in range(10):
#     listlist.append([])


def func(mylist):
    biggestnum = max(mylist)
    biggestten = math.ceil(math.log(biggestnum))

    for i in range(biggestten):
        for j in mylist:
            k = (j // (10**i)) % 10
            (listlist[k]).append(j)
            # print(listlist, k, j)

        mylist = []
        for m in range(10):
            mylist += listlist[m]
            listlist[m] = []

    return mylist


mylist = [8, 100, 34, 22, 65, 30, 4, 55, 18]
print(func(mylist))