import math


def createHashTable(n):
    found = False
    if n <= 2:
        return 2
    while not found:
        flag = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                flag = False
                break
        if flag:
            return n
        n += 1


def insertNumbers(table, nums):
    slots = table * [None]
    res = []
    for i in nums:
        k = 0
        hashValue = i % table
        hashDone = False
        while not hashDone:
            # print(slots, hashValue, i, k)
            if slots[hashValue] == None:
                slots[hashValue] = i
                res.append(hashValue)
                hashDone = True
            else:
                if slots[hashValue] == i:
                    res.append(hashValue)
                    hashDone = True
                else:
                    if k < table - 1:
                        k += 1
                        hashValue = (i + k * k) % table
                    else:
                        break
        if not hashDone:
            res.append('-')
    return ' '.join(map(str, res))


n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
print(insertNumbers(table, nums))