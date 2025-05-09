def dfs(v, graph, visited, stack, command):
    visited[v] = 1
    for u in graph[v]:
        if visited[u] == 0:
            dfs(u, graph, visited, stack, command)
    if command:
        stack.append(v)


def solve(n, graph, transposed_graph):
    visited = [0] * (n+1)
    stack = []

    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i, graph, visited, stack, 1)

    visited = [0] * (n+1)
    res = 0

    while stack:
        v = stack.pop()
        if visited[v] == 0:
            dfs(v, transposed_graph, visited, [], 0)
            res += 1
    print(res)


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        n, m = map(int, lines[0].split())
        graph = [[] for _ in range(n+1)]
        transposed_graph = [[] for _ in range(n+1)]
        for i in range(1, m + 1):
            u, v = map(int, lines[i].split())
            graph[u].append(v)
            transposed_graph[v].append(u)
    solve(n, graph, transposed_graph)