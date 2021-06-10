class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes;
        self.edges = 0;
        self.adj = [];

    def validNode(self,n):
        for i in n:
            if i < 0 or i > self.nodes:
                return False
        return True

    def addEdge(self, n, w):
        if self.validNode([n,w]):
            self.edges += 1;
            self.adj[n].append(w);
            self.adj[w].append(n);

    def adj(self, n):
        if self.validNode(n):
            return self.adj[n]
        return None