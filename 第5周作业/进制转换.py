mydigit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def ToTen(m, num):
    if num == '':
        TenNum = '非法'
        return TenNum
    TenNum = 0
    k = 0
    if num[0] == '-':
        k = 1
    while k < len(str(num)):
        TenNum += (mydigit.index((num[k]))) * (m**(len(str(num)) - k - 1))
        k += 1
    if num[0] == '-':
        TenNum = -TenNum
    return TenNum


def func(m, n, num):
    NewTen = ToTen(m, num)
    if NewTen == '非法':
        return ''
    flag = False
    if NewTen < 0:
        flag = True
        NewTen = -NewTen

    def absfunc(n, NewTen):
        if NewTen < n:
            return mydigit[NewTen]
        else:
            return absfunc(n, NewTen // n) + mydigit[NewTen % n]

    if not flag:
        return absfunc(n, NewTen)
    else:
        return '-' + absfunc(n, NewTen)


print(func(36, 18, '1'))
