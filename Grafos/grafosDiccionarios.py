class Graph:
    def __init__(self):
        self.graph = {}
  
    def add_vertex(self, label):
        if label not in self.graph:
            self.graph[label] = []
    
    def add_edge(self, v1, v2, directed = True):
        self.add_vertex(v1)
        self.add_vertex(v2)
        if(not directed):
            if v1 not in self.graph[v2]:
                self.graph[v2].append(v1)
        if v2 not in self.graph[v1]:
            self.graph[v1].append(v2)


    def determinar(self, v1, v2):
        if v2 in self.graph[v1]:
            return True
        else: 
            pass
        return v2 in self.graph[v1]
    
    def print_graph(self):
        print(self.graph)
    
    def DFS(self, u, visitados =[]):
        if self.graph[u] == []:
            if u not in visitados:
                visitados.append(u)
            return visitados
        else:
            for a in self.graph[u]:
                if a not in visitados:
                    visitados.append(a)
                    self.DFS(a)
            return visitados


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.add_edge("A", "A")
g.add_edge("C", "K")
g.add_edge("K", "C")


g.print_graph()

