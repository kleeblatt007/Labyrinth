import random

class RandomPath(object):
    '''
    Erstellt mit Hilfe der Tiefensuche ein random Pfad
    '''
    def __init__(self, start, G):
        self.marked = [G.nodes]
        for i in range(G.nodes):
            self.marked[i] = False
        self.edgeTo = [G.nodes]
        self.start = start

    def path(self,G):
        self.path(G,self.start)

    def path(self, G, n):
        '''
        Erstellt random Pfad
        :param G: Graph
        :param n: int
        :return:
        '''
        self.marked[n] = True
        rnd = random.shuffle(G.adj(n))
        for w in rnd:
            if not self.marked[w]:
                self.edgeTo[w]=n
                self.path(G,w)

    def pathTo(self,v):
        '''
        gibt Pfad zwischen Knoten und Start zurück
        :param v: int
        :return: list
        '''
        path = []
        while not v == self.start:
            path.append(v)
            v = self.edgeTo[v]

        path.append(self.start)
        return path

    def getEdgeTo(self):
        return self.edgeTo
