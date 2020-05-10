def findAnagrams(s, p):
    res = []
    flag = False
    for i in range(len(s) - len(p) + 1):
        if anagram(s[i:(i + len(p))], p):
            flag = True
            res.append(i)
    if not flag:
        return 'none'
    return ' '.join(map(str, res))


def anagram(a, b):
    return True if sorted(a) == sorted(b) else False


s = input()
p = input()
print(findAnagrams(s, p))