from collections import deque

CUT_OUT = "#"
NOT_CUT = "."
CELL = "@"

VISITED = 1
EMPTY = 0

DIRECTIONS = [(-2, -1), (-1, -2), (-2, 1), (-1, 2),
                (2, -1), (1, -2), (2, 1), (1, 2)]

def solve(maze, n):
    
    positions = [(i, j) for i in range(n) for j in range(n) if maze[i][j] == CELL]
    si, sj = positions[0]
    ei, ej = positions[1]

    visited = [
        [EMPTY for _ in range(n)]
        for _ in range(n)
    ]
    visited[si][sj] = VISITED
    queue = deque()
    queue.append((si, sj))
    prev = [
        [None for _ in range(n)] 
        for _ in range(n)
    ] 
    while queue:
        i, j = queue.popleft()
        if (i, j) == (ei, ej):
            while (i, j) != (si, sj):
                maze[i][j] = "@"
                i, j = prev[i][j]
            maze[si][sj] = "@"
            return maze
        
        for di, dj in DIRECTIONS:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] != CUT_OUT and not visited[ni][nj]:
                    visited[ni][nj] = VISITED
                    prev[ni][nj] = (i, j)
                    queue.append((ni, nj))
    return "Impossible"

if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        maze = [list(f.readline().rstrip()) for _ in range(n)]

    res = solve(maze, n)
    if res == "Impossible":
        print("Impossible")
    else:
        for row in res:
            print(''.join(row))
