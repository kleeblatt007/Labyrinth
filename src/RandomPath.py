import random


class RandomPath(object):
    '''
    Erstellt mit Hilfe der Tiefensuche ein random Pfad
    '''

    def __init__(self, start, G):
        self.marked = []
        self.edgeTo = [0 for x in range(G.getNodes())]
        for i in range(G.getNodes()):
            self.marked.append(False)
        self.start = start

    def path(self, G):
        '''
        scheint nicht zu funktionieren
        '''
        self.path(G, self.start)

    def path(self, G, n):
        '''
        Erstellt random Pfad
        :param G: Graph
        :param n: int
        :return:
        '''
        self.marked[n] = True
        rnd = G.getAdj(n)
        random.shuffle(rnd)
        for w in rnd:
            if not self.marked[w]:
                self.edgeTo[w] = n
                self.path(G, w)

    def pathTo(self, v):
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
