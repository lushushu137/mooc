def myeval(x, op, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y


backup = dict({})


def cal(nums, ops):
    if len(ops) == 0:
        return {nums[0]}
    if len(ops) == 1:
        return {myeval(nums[0], ops[0], nums[1])}
    res = set()
    for i in range(len(ops)):
        leftnums = nums[:i + 1]
        leftop = ops[:i]
        rightnums = nums[i + 1:]
        rightop = ops[i + 1:]
        leftres = cal(leftnums, leftop)
        rightres = cal(rightnums, rightop)
        for l in leftres:
            for r in rightres:
                res.add(myeval(l, ops[i], r))
    return res


def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
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

    res = sorted(list(set(cal(nums, ops))))
    return ','.join([str(j) for j in res])


expr = input()
print(findWays(expr))
