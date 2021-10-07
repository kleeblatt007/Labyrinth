from Graph import Graph
from RandomPath import RandomPath
from DepthFirstPath import DepthFirstPath
from Coordinate import Coordinate
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# from pprint import pprint
# import numpy as np


class Labyrinth(object):
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
        s = 0
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
                    if x == 0:
                        m.addEdge(s, s + 1)
                        m.addEdge(s, s + self.N)
                        m.addEdge(s, s - self.N)
                    elif x == self.N - 1:
                        m.addEdge(s, s - 1)
                        m.addEdge(s, s + self.N)
                        m.addEdge(s, s - self.N)
                    else:
                        m.addEdge(s, s + 1)
                        m.addEdge(s, s - 1)
                        m.addEdge(s, s + self.N)
                        m.addEdge(s, s - self.N)
                s += 1
        #m.printGraph()
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

    def printPath(self, path,e):
        '''
        Stellt ein Graphen mit path, mit Hilfe von plt.plot, graphisch dar
        :param path: vorher erstellter path
        :param e: Endknoten
        '''
        edges = path.pathTo(e)
        for n in range(self.graph.getNodes()):
            for v in self.graph.getAdj(n):
                c1 = self.nodeToCoordinate(n)
                c2 = self.nodeToCoordinate(v)
                plt.plot(c1.x,c1.y,'o')
                x = [c1.X(), c2.X()]
                y = [c1.Y(), c2.Y()]
                plt.plot(x, y, "black", linewidth=3.0)
        for x in range(len(edges)-1,1,-1):
            c1 = self.nodeToCoordinate(edges[x])
            c2 = self.nodeToCoordinate(edges[x-1])
            # plt.plot(c1.x,c1.y,'o')
            x = [c1.X(), c2.X()]
            y = [c1.Y(), c2.Y()]
            plt.plot(x, y, "red", linewidth=3.0)
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
        self.printPath(path,e)
        return path.pathTo(e)

    def nodeToCoordinate(self, n):
        '''
        Errechnet Koordinaten des Knoten
        :param n: int
        :return: Coordinate
        '''
        if n == 0:
            c = Coordinate(0, self.N - 1)
            return c

        x = n % self.N
        y = self.N - 1 - int(n / self.N)
        c = Coordinate(x, y)
        return c

    def printLab(self):
        '''
        Stellt das Labyrint mit Hilfe von plt.plot graphisch dar
        '''
        # x = 0
        # y = self.N-1
        for n in range(self.graph.getNodes()):
            # xArray = []
            # yArray = []
            # xArray.append(x)
            # yArray.append(y)
            for v in self.graph.getAdj(n):
                c1 = self.nodeToCoordinate(n)
                c2 = self.nodeToCoordinate(v)
                plt.plot(c1.x,c1.y,'o')
                x = [c1.X(), c2.X()]
                y = [c1.Y(), c2.Y()]
                plt.plot(x, y, "black", linewidth=3.0)

        plt.show()

    def printLabPlotly(self):
        fig = go.Figure()

        for n in range(self.graph.getNodes()):
            nX = self.nodeToCoordinate(n).x
            nY = self.nodeToCoordinate(n).y
            for v in self.graph.getAdj(n):
                xList = []
                yList = []
                xList.append(nX)
                xList.append(self.nodeToCoordinate(v).x)
                yList.append(nY)
                yList.append(self.nodeToCoordinate(v).y)

                df = pd.DataFrame(dict(
                    x=xList,
                    y=yList
                ))
                fig.add_trace(go.Scatter(x=xList, y=yList, mode="lines"))
        fig.show()

    def labToTxt(self, end):
        '''
        Erstellt aus dem Labyrinth eine Abbildung auf ein zweidimensionales Array
        und erstellt eine txt Datei. 1 = freier Weg, 0 = Wand, 2 = Ziel
        :param end: Ziel-Knoten
        '''
        a = [[0 for i in range(self.N * 2 +1)] for x in range(self.N * 2 + 1)]
        y = 1
        for n in range(self.graph.getNodes()):
            c = self.nodeToCoordinate(n)
            x = c.X() * 2
            if x == 0:
                x = 1
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
            a[end[0]][end[1]] = 2
        # pprint(a)
        # b = np.array(a)
        # np.savetxt('Lab.txt', b)
        with open('Lab.txt', 'w') as file:
            for row in a:
                file.write(' '.join([str(c) for c in row]) + '\n')
