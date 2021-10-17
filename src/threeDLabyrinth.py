from Graph import Graph
from RandomPath import RandomPath
from DepthFirstPath import DepthFirstPath
from Coordinate import Coordinate
import matplotlib.pyplot as plt
import math
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# from pprint import pprint
# import numpy as np


class threeDLabyrinth(object):
    def __init__(self, N, start):
        self.N = N
        self.graph = Graph(pow(N, 3))
        self.start = start
        self.coordinates = []
        for x in range(self.graph.getNodes()):
            c = Coordinate(0, 0, 0)
            self.coordinates.append(c)
        self.build()


    def grid(self):
        '''
        Baut ein Gitter, was für den RandomPath benötigt wird. Jeder Knoten (außer die Ränder) sind mit den Knoten
        rechts, links, unten und über ihnen verbunden.
        :return: Graph
        '''
        m = Graph(pow(self.N, 3))
        s = 0
        for z in range(self.N):
            for y in range(self.N):
                for x in range(self.N):
                    if z == 0:
                        if y == 0:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                        elif y == self.N - 1:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                        else:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                    elif z == self.N - 1:
                        if y == 0:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                        elif y == self.N - 1:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                        else:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s - pow(self.N, 2))
                    else:
                        if y == 0:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                        elif y == self.N - 1:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                        else:
                            if x == 0:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                            elif x == self.N - 1:
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                            else:
                                m.addEdge(s, s + 1)
                                m.addEdge(s, s - 1)
                                m.addEdge(s, s + self.N)
                                m.addEdge(s, s - self.N)
                                m.addEdge(s, s + pow(self.N, 2))
                                m.addEdge(s, s - pow(self.N, 2))
                    self.coordinates[s].setCoordinates(x, self.N - 1 - y, z)
                    s += 1
        return m

    def build(self):
        '''
        Bildet ein Graph als Labyrinth. Dabei wird über ein grid ein Pfad per zufälliger Tiefensuche gebildet.
        :return:
        '''
        if self.graph.getNodes() <= 2:
            return
        G = RandomPath(self.start, self.graph)
        G.path(self.grid(), self.start)
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

    def printPath(self, path, e):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        edges = path.pathTo(e)
        for n in range(self.graph.getNodes()):
            # xArray = []
            # yArray = []
            # xArray.append(x)
            # yArray.append(y)
            for v in self.graph.getAdj(n):
                c1 = self.nodeToCoordinate(n)
                c2 = self.nodeToCoordinate(v)
                x = [c1.X(), c2.X()]
                y = [c1.Y(), c2.Y()]
                z = [c1.Z(), c2.Z()]
                ax.plot(x, y, z, "black", linewidth=3.0)
            #plt.show()
        for x in range(len(edges) - 1, 1, -1):
            c1 = self.nodeToCoordinate(edges[x])
            c2 = self.nodeToCoordinate(edges[x - 1])
            # plt.plot(c1.x,c1.y,'o')
            x = [c1.X(), c2.X()]
            y = [c1.Y(), c2.Y()]
            z = [c1.Z(), c2.Z()]
            ax.plot(x, y, z, "red", linewidth=3.0)

        plt.show()

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
        path.path(self.graph, s)
        self.printPath(path, e)
        return path.pathTo(e)

    def nodeToCoordinate(self, n):
        '''
        Errechnet Koordinaten des Knoten
        :param n: int
        :return: Coordinate
        '''
        if n == 0:
            c = Coordinate(0, self.N - 1, 0)
            return c

        #x = n % self.N
        #y = self.N - 1 - int(n / self.N)
        #z = math.floor(n/self.N)%self.N
        #c = Coordinate(x, y, z)
        return self.coordinates[n]

    def printLab(self):
        # x = 0
        # y = self.N-1
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        for n in range(self.graph.getNodes()):
            # xArray = []
            # yArray = []
            # xArray.append(x)
            # yArray.append(y)
            for v in self.graph.getAdj(n):
                c1 = self.nodeToCoordinate(n)
                c2 = self.nodeToCoordinate(v)
                #ax.plot(c1.X(), c1.Y(), c1.Z(),'o', color='black')
                x = [c1.X(), c2.X()]
                y = [c1.Y(), c2.Y()]
                z = [c1.Z(), c2.Z()]
                ax.plot(x, y, z, "black", linewidth=3.0)

        plt.show()



    def labToTxt(self):
        a = [[0 for i in range(self.N * 2 - 1)] for x in range(self.N * 2 - 1)]
        y = 0
        for n in range(self.graph.getNodes()):
            c = self.nodeToCoordinate(n)
            x = c.X() * 2
            a[y][x] = 1
            for v in self.graph.getAdj(n):
                i = v - n
                if i == 1:
                    a[y][x + 1] = 1
                elif i == -1:
                    a[y][x - 1] = 1
                elif i > 0:
                    a[y + 1][x] = 1
                else:
                    a[y - 1][x] = 1
            if c.X() == self.N - 1:
                y += 2
        # pprint(a)
        # b = np.array(a)
        # np.savetxt('Lab.txt', b)
        with open('Lab.txt', 'w') as file:
            for row in a:
                file.write(' '.join([str(c) for c in row]) + '\n')
