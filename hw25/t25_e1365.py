import sys
from collections import deque
INF = sys.maxsize

def getWay(matrix, start, end):
    n = len(matrix)
    distances = [INF for _ in range(n)]
    distances[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        i = queue.popleft()
        for j in range(n):
            weight = matrix[i][j]
            if weight != -1 and distances[j] > distances[i] + weight:
                distances[j] = distances[i] + weight
                queue.append(j)

    if distances[end] != INF:
        return distances[end]
    else:
        return -1


if __name__ == '__main__':
    n, s, f = map(int, list(input().split()))
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(getWay(matrix, s-1, f-1))
