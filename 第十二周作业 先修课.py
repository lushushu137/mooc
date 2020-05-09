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

def buildGraph(n, pre):
    school = Graph()
    for i in range(n):
        school.addVertex(i)
    for k in pre:
        school.addEdge(k[0], k[1])
    return school


def dfs(course):
    course.color = 'grey'
    for nextcourse in course.connectedTo:
        if nextcourse.color == 'white':
            dfs(nextcourse)
        if nextcourse.color == 'grey':
            return False
    course.color = 'black'
    


def canFinish(graph):
    for course in graph:
        boolval = dfs(course)
        if boolval == False:
            return False
    return True
            
        
    
    

n = int(input())
pre = input()
schoolGraph = buildGraph(n,pre)
print(canFinish(schoolGraph))


