def func(rates):
    candies1 = [1] * len(rates)
    candies2 = [1] * len(rates)
    candies = [1] * len(rates)
    for i in range(len(rates) - 1):#正向遍历，只处理右>左的情况
        if rates[i] < rates[i + 1]:
            candies1[i + 1] = candies1[i] + 1

    for i in range(len(rates) - 1, 0, -1):#反向遍历，只处理右<左的情况
        if rates[i - 1] > rates[i]:
            candies2[i - 1] = candies2[i] + 1

    for i in range(len(candies)):
        candies[i] = max(candies1[i], candies2[i])

    return sum(candies)


print(func([1, 2, 2]))
