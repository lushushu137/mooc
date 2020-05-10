def func(N, knownresults):
    arr = [1, 2, 3, 4]
    res = 0
    if N == 0:
        knownresults[N] = 1
        return 1
    elif N < 0:
        return 0
    elif knownresults[N] > 0:
        return knownresults[N]
    for i in arr:
        print(i, N, knownresults)
        res += func(N - i, knownresults)
        knownresults[N] = res
    return res


print(func(5, [0, 0, 0, 0, 0, 0]))
