from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.vertices = {i: set() for i in range(1, n + 1)}
    
    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)
    

    def bfs(self, start):
        visited = set()
        queue = deque()
        res = []
        queue.append(start)
        visited.add(start)

        while queue:
            u = queue.popleft()
            for neighbour in self.vertices[u]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    res.append((u, neighbour))
                    queue.append(neighbour)
        
        return res
                

if __name__ == '__main__':
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v) 
        res = graph.bfs(1)
    for u, v in res:
        print(u, v)
