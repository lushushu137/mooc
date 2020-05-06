def findAnagrams(s, p):
    mydict = {}
    output = []
    for k in range(len(p)):
        mydict[k] = p[k]
    i = 0
    while i < len(s) - len(p):
        flag = True
        j = 0
        while j in range(0, len(p)):
            print(i + j, s[j + i])
            if s[j + i] not in mydict.values():
                flag = False
                break
            else:
                j += 1
        if flag:
            output.append(i)
        i += 1
    if output == []:
        return 'none'
    else:
        realoutput = [str(k) for k in output]
        return ' '.join(realoutput)


s = input()
p = input()
print(findAnagrams(s, p))