import sys
sys.setrecursionlimit(10**5)

# WHITE = 0
# GRAY = 1
# BLACK = 2

def dfs(graph, v, color, res):
    color[v] = 1
    for u in graph[v]:
        if color[u] == 1:
            return False
        if color[u] == 0:
            if not dfs(graph, u, color, res):
                return False
    color[v] = 2
    res.append(v)
    return True

def solve(graph, n, m):
    color = [0] * (n+1)
    res = []
    r = True
    for v in range(1, n+1):
        if color[v] == 0:
            if not dfs(graph, v, color, res):
                r = False
                break
    if r:
        print(*(reversed(res)))
    else:
        print(-1)


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
    solve(graph, n, m)
