import Graph
import RandomPath
import DepthFirstPath
import Coordinate
import math
import matplotlib.pyplot as plt


class Lab(object):
    def __init__(self, N, start):
        self.N = N
        self.graph = Graph(pow(N, 2))
        self.start = start
        self.build()

    def grid(self):
        '''
        Baut ein Gitter, was für den RandomPath benötigt wird. Jeder Knoten (außer die Ränder) sind mit den Knoten
        rechts, links, unten und über ihnen verbunden.
        :return: Graph
        '''
        m = Graph(pow(self.N, 2))
        s = self.start
        for y in range(self.N):
            for x in range(self.N):
                if y == 0:
                    if x == 0:
                        m.addEdge(s, s + 1)
                        m.addEdge(s, s + self.N)
                    elif x == self.N - 1:
                        m.addEdge(s, s - 1)
                        m.addEdge(s, s + self.N)
                    else:
                        m.addEdge(s, s + 1)
                        m.addEdge(s, s - 1)
                        m.addEdge(s, s + self.N)
                elif y == self.N - 1:
                    if x == 0:
                        m.addEdge(s, s + 1)
                        m.addEdge(s, s - self.N)
                    elif x == self.N - 1:
                        m.addEdge(s, s - 1)
                        m.addEdge(s, s - self.N)
                    else:
                        m.addEdge(s, s + 1)
                        m.addEdge(s, s - 1)
                        m.addEdge(s, s - self.N)
                else:
                    m.addEdge(s, s + 1)
                    m.addEdge(s, s - 1)
                    m.addEdge(s, s + self.N)
                    m.addEdge(s, s - self.N)
                s += 1

        return m

    def build(self):
        '''
        Bildet ein Graph als Labyrinth. Dabei wird über ein grid ein Pfad per zufälliger Tiefensuche gebildet.
        :return:
        '''
        if self.graph.getNodes() <= 2:
            return
        G = RandomPath(self.graph, self.start)
        G.path(self.grid())
        a = G.getEdgeTo()
        for i in range(len(a)):
            if i == self.start:
                continue
            self.graph.addEdge(i, a[i])

    def hasEdge(self, v, w):
        '''
        Prüft, ob zwei Knoten durch eine Kante verbunden ist.
        :param v: int
        :param w: int
        :return: boolean
        '''
        if self.graph.validNode(v) and self.graph.validNode(w):
            for x in self.graph.adj(v):
                if x == w:
                    return True
        return False

    def findWay(self, s, e):
        '''
        Ein Pfad wird durch Tiefensuche(DepthFirstPath) zwischen zwei Knoten gesucht
        :param s: int
        :param e: int
        :return: list
        '''
        if not self.graph.validNode(s) or not self.graph.validNode(e):
            return
        path = DepthFirstPath(self.graph, s)
        path.path(self.graph)
        return path.pathTo(e)

    def nodeToCoordinate(self, n):
        '''
        Errechnet Koordinaten des Knoten
        :param n: int
        :return: Coordinate
        '''
        if n == 0:
            c = Coordinate(0, 0)
            return c

        x = int(math.ceil(n / self.N) - 1)
        y = int(self.N / int(n / self.N))
        c = Coordinate(x, y)
        return c

    def __str__(self):
        # x = 0
        # y = self.N-1
        for n in range(self.graph.getNodes()):
            # xArray = []
            # yArray = []
            # xArray.append(x)
            # yArray.append(y)
            for v in self.graph.adj(n):
                c1 = self.nodeToCoordinate(n)
                c2 = self.nodeToCoordinate(v)
                plt.plot({c1.X, c2.X}, {c1.Y, c2.Y})

        # x += 1
        # if x == self.N:
        #     y -= 1
        #     x = 0