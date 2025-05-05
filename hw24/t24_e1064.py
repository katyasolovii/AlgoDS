from collections import deque

CUT_OUT = "#"
NOT_CUT = "."
CELL = "@"

VISITED = 1
EMPTY = 0

KNIGHT_MOVES = [(-2, -1), (-1, -2), (-2, 1), (-1, 2),
                (2, -1), (1, -2), (2, 1), (1, 2)]

def bfs(maze, n):

    visited = [
        [EMPTY for _ in range(n)] 
        for _ in range(n)
    ]
    prev = [
        [None for _ in range(n)] 
        for _ in range(n)
    ]

    positions = []
    for i in range(n):
        for j in range(n):
            if maze[i][j] == CELL:
                positions.append((i, j))
    
    start, end = positions[0], positions[1]
    
    queue = deque()
    si, sj = start
    ei, ej = end
    
    queue.append((si, sj))
    visited[si][sj] = VISITED
    
    while queue:
        i, j = queue.popleft()
        
        if (i, j) == (ei, ej):
            path_i, path_j = ei, ej
            while (path_i, path_j) != (si, sj):
                if maze[path_i][path_j] != CELL:
                    maze[path_i][path_j] = "@"
                path_i, path_j = prev[path_i][path_j]
            maze[si][sj] = "@"
            return maze
        
        for di, dj in KNIGHT_MOVES:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] != CUT_OUT and visited[ni][nj] == EMPTY:
                    visited[ni][nj] = VISITED
                    prev[ni][nj] = (i, j) 
                    queue.append((ni, nj))
    
    return "Impossible"

if __name__ == '__main__':
    with open("input.txt") as f:
        n = int(f.readline())
        maze = []
        
        for i in range(n):
            row = list(f.readline().rstrip())
            maze.append(row)
    
    result = bfs(maze, n)
    
    if result == "Impossible":
        print("Impossible")
    else:
        for row in result:
            print(''.join(row))
