from collections import deque


class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = []
        self.color = 'white'

    def addNbr(self, nbr):
        self.connectedTo.append(nbr)

    def allKeys(self):
        return [v.id for v in self.connectedTo]


class Graph():
    def __init__(self):
        self.vertList = {}

    def addVertex(self, key):
        self.vertList[key] = Vertex(key)

    def addEdge(self, a, b):
        if a not in self.vertList:
            self.addVertex(a)
        if b not in self.vertList:
            self.addVertex(b)
        self.vertList[a].addNbr(self.vertList[b])

    def __contains__(self, n):
        return n in self.vertList

    def __iter__(self):
        for key in self.vertList:
            yield self.vertList[key]


def canVisitAll(rooms):
    room = Graph()
    for i in range(len(rooms)):
        if i not in room:
            room.addVertex(i)
        for j in range(len(rooms[i])):
            if rooms[i][j] not in room:
                room.addVertex(rooms[i][j])
            room.addEdge(i, rooms[i][j])

    mydeque = deque()
    mydeque.append(room.vertList[0])
    while mydeque:
        currRoom = mydeque.popleft()
        currRoom.color = 'black'
        nextRooms = currRoom.connectedTo
        for n in nextRooms:
            if n.color != 'black':
                mydeque.append(n)
                n.color = 'grey'
    for n in room:
        if n.color == 'white':
            return False
    return True


rooms = eval(input())
print(canVisitAll(rooms))