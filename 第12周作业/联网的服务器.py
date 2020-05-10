def connectedServer(alist):
    myset = set()
    for row in range(len(alist)):
        first = (-1,-1)
        flag = False
        for server in range(len(alist[row])):
            if alist[row][server] == 1 and not flag:
               flag = True
               first = (row, server)
            elif alist[row][server] == 1 and flag:
                myset.add((row,server))
                myset.add(first)
    for col in range(len(alist[0])):
        first = (-1, -1)
        flag = False
        for server in range(len([j[col] for j in alist])):
            if alist[server][col] == 1 and not flag:
               flag = True
               first = (server, col)
            elif alist[server][col] == 1 and flag:
                myset.add((server,col))
                myset.add(first)

    return len(myset)

print(connectedServer([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
            
