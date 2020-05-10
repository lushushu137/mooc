def func(mylist):
    start = 0
    end = 0
    output = []
    for cur in range(len(mylist)):
        # print('cur', cur)
        while mylist[start] < mylist[cur] - 10000:
            start += 1
            # print('start', mylist[start], mylist[cur])
        while end < len(mylist) and mylist[end] <= mylist[cur]:
            end += 1
            # print('end', mylist[cur], mylist[end])

        output.append(end - start)
        # print('output', output)
    return output


mylist = eval(input())
print(func(mylist))