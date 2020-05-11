def hanoi_3(height):
    return 2**height - 1


mydict = {}


def hanoi_4(height):
    if height == 0:
        res = 0
    elif height == 1:
        res = 1
    else:
        res = 999999999

        for i in range(1, height):
            if height - i in mydict:
                hanoi_4_val = mydict[height - i]
            else:
                hanoi_4_val = hanoi_4(height - i)
                mydict[height - i] = hanoi_4_val
            res = min(2 * hanoi_4_val + hanoi_3(i), res)
    return res


'''
动态规划版
def kun(T):
    h4 = [0, 1, 3]
    h3 = [0, 1, 3]

    for n in range(3, T+1):
        h3.append(2**n - 1)
        res = 999999999999999
        for i in range(1, n):
            tmp = h4[n-i] * 2 + h3[i]
            if tmp < res:
                res = tmp
        h4.append(res)
    return h4[T]
'''

a = int(input())
print(hanoi_4(a))
