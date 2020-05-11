def seperate(expr):
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)
    return nums, ops


def calc(a, oper, b):
    if oper == "+":
        return a + b
    if oper == '-':
        return a - b
    if oper == '*':
        return a * b


res = []


def findWays(nums, ops):
    global res
    if len(ops) == 1:
        res += [calc(nums[0], ops[0], nums[1])]
        # print('res:', res)
    else:
        for i in range(len(nums) - 1):
            # print(nums, ops)
            temp = calc(nums[i], ops[i], nums[i + 1])
            newnums = nums[:i] + [temp] + nums[i + 2:]
            newops = ops[:i] + ops[i + 1:]
            # print('newnums:', newnums, 'newops:', newops)
            res += findWays(newnums, newops)
    return sorted(list(set(res)))


expr = input()
nums = seperate(expr)[0]
ops = seperate(expr)[1]
finalres = ','.join([str(j) for j in findWays(nums, ops)])
print(finalres)
