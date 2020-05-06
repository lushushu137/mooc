class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = []

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


def trustedByAll(town, judge):
    flag = True
    for key in town.vertList:
        if judge in town.vertList[key].allKeys():
            continue
        else:
            if judge != key:
                flag = False
                break
            else:
                continue
    return flag


def findJudge(N, trust):
    town = Graph()
    found = False
    for i in range(1, N + 1):
        town.addVertex(i)
    for j in trust:
        town.addEdge(j[0], j[1])
    for key in town.vertList:
        if town.vertList[key].connectedTo == [] and trustedByAll(town, key):
            found = True
            return key
    if not found:
        return -1


N = int(input())
trust = eval(input())
print(findJudge(N, trust))