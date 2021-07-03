class DepthFirstPath(object):

    def __init__(self, G, start):
        self.start = start
        self.marked = [G.nodes]
        for i in range(G.nodes):
            self.marked[i] = False
        self.edgeTo = [G.nodes]
        self.distTo = [G.nodes]

    def path(self, G):
        self.path(G, self.start)

    def path(self, G, n):
        self.marked[n] = True
        self.preoreder.append(n)
        for w in G.adj(n):
            if not self.marked[w]:
                self.edgeTo[w] = n
                self.path(G, w)
        self.postorder.append(n)

    def pathTo(self, v):
        path = []
        while not v == self.start:
            path.append(v)
            v = self.edgeTo[v]

        path.append(self.start)
        return path

    def getEdgeTo(self):
        return self.edgeTo