import sys

INF = sys.maxsize

def findDistance(n, edges):
    distances = [INF for _ in range(n + 1)]
    start = 0
    distances[start] = 0

    for _ in range(n - 1):
        updated = False
        for i, j, w in edges:
            if distances[j] > distances[i] + w:
                distances[j] = distances[i] + w
                updated = True
        if not updated:
            break

    for i, j, w in edges:
        if distances[j] > distances[i] + w:
            return "possible"
    return "not possible"


if __name__ == '__main__':
    n, m = map(int, list(input().split()))
    edges = []
    for _ in range(m):
        start, end, weight = list(map(int, input().split()))
        edges.append((start, end, weight))
    print(findDistance(n, edges))
    
