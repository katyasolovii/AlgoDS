from collections import deque

def solve(n, graph, edges, edges_request):

    for i in edges_request:
        visited = [0] * (n+1)
        set_edges = set(i)
        queue = deque()
        queue.append(1)
        visited[1] = 1
        count = 1

        # bdf
        while queue:
            u = queue.popleft()
            for v, index in graph[u]:
                if index in set_edges:
                    continue
                if visited[v] == 0:
                    visited[v] = 1
                    count += 1
                    queue.append(v)

        if count == n:
            print("Connected")
        else:
            print("Disconnected")

if __name__ == '__main__':
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        edges = []
        graph = [[] for _ in range(n + 1)]

        for i in range(1, m + 1):
            a, b = map(int, f.readline().split())
            graph[a].append((b, i))
            graph[b].append((a, i))
            edges.append((a, b))

        k = int(f.readline())
        edges_request = []

        for _ in range(k):
            data = list(map(int, f.readline().split()))
            edges_request.append(data[1:])

        solve(n, graph, edges, edges_request)