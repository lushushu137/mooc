def merge(alist, blist):
    subleng = 2
    res = blist
    while res == blist:
        sublist = [
            sorted(alist[i:i + subleng])
            for i in range(0, len(alist), subleng)
        ]
        res = []
        for ls in sublist:
            for num in ls:
                res.append(num)
        subleng = subleng * 2
    return res


merge([3, 1, 2, 8, 7, 5, 9, 4, 6, 0], [1, 3, 2, 8, 5, 7, 4, 9, 0, 6])
