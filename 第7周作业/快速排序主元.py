def func(mylist):
    answerlist = []
    for i in range(len(mylist)):
        leftmark = 0
        rightmark = len(mylist) - 1
        flag1 = True
        flag2 = True

        while flag1 and leftmark < i:
            # print('leftmark and i:', leftmark, i)
            if mylist[leftmark] < mylist[i]:
                leftmark += 1
            else:
                flag1 = False
        # print('flag1:', flag1)
        while flag2 and rightmark > i:
            # print('rightmark and i:', rightmark, i)
            if mylist[rightmark] > mylist[i]:
                rightmark -= 1
            else:
                flag2 = False
        # print('flag2:', flag2)
        if flag1 and flag2:
            answerlist.append(mylist[i])
            # print('when this leftmark and rightmark, answerlist:', answerlist)
    return answerlist


def output(answerlist):
    return str(len(answerlist)) + '\n' + " ".join([str(x) for x in answerlist])


heylist = input()
ohlist = [int(i) for i in heylist.split()]
# print(ohlist)
print(output(func(ohlist)))