class Graph(object):
    def __init__(self, nodes):
        self.nodes = int(nodes)
        self.edges = 0
        self.adj = [[]for x in range(nodes)]

    def validNode(self, n):
        '''
        Prüft ob Knoten innerhalb des Graphen liegt
        :param n: int
        :return: boolean
        '''
        if n.__class__ == int:
            if n < 0 or n > self.nodes:
                return False
        else:
            for x in n:
                if x < 0 or x > self.nodes:
                    return False
        return True

    def addEdge(self, n, w):
        '''
        Fügt Kanten zwischen zwei Knoten hinzu. Die Kanten sind ungerichtet, dadurch muss adj für beide Knoten
        aktualiesiert werden
        :param n: int
        :param w: int
        :return:
        '''
        if self.validNode([n,w]):
            #if self.adj[n].__contains__(w):
                #return
            self.edges += 1
            self.adj[n].append(w)
            self.adj[w].append(n)

    def getAdj(self, n):
        '''
        gibt adjazierende Knoten für Knoten n zurück
        :param n: int
        :return: list
        '''
        if self.validNode(n):
            return self.adj[n]
        return None

    def getNodes(self):
         x = self.nodes
         return x

    def getEdges(self):
        return self.edges