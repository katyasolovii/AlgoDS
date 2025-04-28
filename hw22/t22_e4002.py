from collections import deque


class Graph:
    
    def __init__(self, n):
        self.n = n
        self.vertices = {i: set() for i in range(1, n + 1)}
    
    def add_edge(self, u, v):
        self.vertices[u].add(v)
        self.vertices[v].add(u)

    def bfs(self, start):
        values = [-1 for _ in range(n+1)]
        queue = deque()
        values[start] = 0 
        queue.append(start)

        while queue:
            i = queue.popleft()
            for j in self.vertices[i]:
                if values[j] == -1: 
                    values[j] = 1 - values[i] 
                    queue.append(j)
                elif values[j] == values[i]:  
                    return False 
        return True


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        n, m = map(int, f.readline().split())  
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u, v) 

        for i in range(1, n+1):
            if not graph.bfs(i): 
                print("NO")
                break
        else:
            print("YES")
