import Graph
import random

class RandomPath(object):
    def __init__(self, start, G):
        self.marked = [G.nodes]
        for i in range(G.nodes):
            self.marked[i] = False
        self.edgeTo = [G.nodes]
        self.start = start

    def
    def path(self, G, n):
        self.marked[n] = True
        rnd = random.shuffle(G.adj(n))
        for w in rnd:
            if not self.marked[w]:
                self.edgeTo[w]=n
                self.path(G,w)