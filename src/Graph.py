class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = 0
        self.adj = []

    def validNode(self, n):
        '''
        Prüft ob Knoten innerhalb des Graphen liegt
        :param n: int
        :return: boolean
        '''
        for i in n:
            if i < 0 or i > self.nodes:
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
            if self.adj(n).__contains(w):
                return
            self.edges += 1
            self.adj[n].append(w)
            self.adj[w].append(n)

    def adj(self, n):
        '''
        gibt adjazierende Knoten für Knoten n zurück
        :param n: int
        :return:
        '''
        if self.validNode(n):
            return self.adj[n]
        return None

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges