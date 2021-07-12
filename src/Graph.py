import math
from Coordinate import Coordinate
import matplotlib.pyplot as plt

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
            if len(self.adj[n]) > 0:
                if self.adj[n].__contains__(w):
                    return
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

    def nodeToCoordinate(self, n):
        '''
        Errechnet Koordinaten des Knoten
        :param n: int
        :return: Coordinate
        '''
        if n == 0:
            c = Coordinate(0, math.sqrt(self.nodes) - 1)
            return c

        x = n % math.sqrt(self.nodes)
        y = math.sqrt(self.nodes) - 1 - int(n / math.sqrt(self.nodes))
        c = Coordinate(x, y)
        return c

    def printGraph(self):
        for n in range(self.nodes):
            # xArray = []
            # yArray = []
            # xArray.append(x)
            # yArray.append(y)
            for v in self.adj[n]:
                c1 = self.nodeToCoordinate(n)
                c2 = self.nodeToCoordinate(v)
                plt.plot(c1.x,c1.y,'o')
                x = [c1.X(), c2.X()]
                y = [c1.Y(), c2.Y()]
                plt.plot(x, y, "black")

        plt.show()