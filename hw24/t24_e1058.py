from collections import deque

NOT_FILLED = "*"
FILLED = "."

VISITED = 1
EMPTY = 0

DIRECTIONS = ((0, -1), (-1, 0), (0, 1), (1, 0))

def solve(maze, m, n):
    visited = [
        [EMPTY for _ in range(n)] 
        for _ in range(m)
    ]
    max_size = 0
    for i in range(m):
        for j in range(n):
            if maze[i][j] == FILLED and visited[i][j] == EMPTY:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = VISITED
                size = 1  

                while queue:
                    ci, cj = queue.popleft()
                    for di, dj in DIRECTIONS:
                        ni = ci + di
                        nj = cj + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            if maze[ni][nj] == FILLED and visited[ni][nj] == EMPTY:
                                visited[ni][nj] = VISITED
                                queue.append((ni, nj))
                                size += 1

                max_size = max(max_size, size)
    return max_size

if __name__ == '__main__':
    with open("input.txt") as f:
        n, m, k = map(int, f.readline().split()) 
        plots = []
        for _ in range(k):
            r, c = map(int, f.readline().split())
            plots.append((r - 1, c - 1)) 

    maze = [
        [NOT_FILLED for _ in range(m)] 
        for _ in range(n)
    ]
    
    for r, c in plots:
        maze[r][c] = FILLED
    print(solve(maze, n, m))
