from collections import deque

def solve(n, graph):
    visited = [0] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if visited[i] == 0:
            queue = deque()
            queue.append(i)
            visited[i] = 1
            component = []
            
            while queue:
                u = queue.popleft()
                component.append(u)
                for v in graph[u]:
                    if visited[v] == 0:
                        visited[v] = 1
                        queue.append(v)
            components.append(component)
    print(len(components))
    for j in components:
        print(len(j))
        print(*j)


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        n, m = map(int, lines[0].split())
        graph = [[] for _ in range(n+1)]
        for i in range(1, m + 1):
            u, v = map(int, lines[i].split())
            graph[u].append(v)
            graph[v].append(u)
    solve(n, graph)
