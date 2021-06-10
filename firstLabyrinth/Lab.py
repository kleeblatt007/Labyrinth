import Graph

class Lab(object):
    def __init__(self, N, start):
        self.N = N
        self.graph = Graph(pow(N,2))
        self.start = start

    def build(self):
        s = self.start
        for y in range(self.N):
            for x in range(self.N):
                if y == 0:
                    if x == 0:
                        self.graph.addEdge(s,s+1)
                        self.graph.addEdge(s, s + self.N)
                    elif x == self.N-1:
                        self.graph.addEdge(s, s - 1)
                        self.graph.addEdge(s, s + self.N)
                    else:
                        self.graph.addEdge(s, s + 1)
                        self.graph.addEdge(s, s - 1)
                        self.graph.addEdge(s, s + self.N)
                elif y == self.N-1:
                    if x == 0:
                        self.graph.addEdge(s, s + 1)
                        self.graph.addEdge(s, s - self.N)
                    elif x == self.N-1:
                        self.graph.addEdge(s, s - 1)
                        self.graph.addEdge(s, s - self.N)
                    else:
                        self.graph.addEdge(s, s + 1)
                        self.graph.addEdge(s, s - 1)
                        self.graph.addEdge(s, s - self.N)
                else:
                    self.graph.addEdge(s, s + 1)
                    self.graph.addEdge(s, s - 1)
                    self.graph.addEdge(s, s + self.N)
                    self.graph.addEdge(s, s - self.N)


