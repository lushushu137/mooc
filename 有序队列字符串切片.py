def func(S):
    # output = ''
    # for i in S:
    #     output += i
    output = S

    k = 0
    item = ''
    while k < len(S):
        item = S[1:] + S[0]
        S = item
        # print(output, k, item)
        if item < output:
            output = item
        k += 1
    return output


print(func('cba'))