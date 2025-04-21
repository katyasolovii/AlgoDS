def solve(n, matrix):
    m = []
    res = 0
    for i in range(n):
        deg = 0
        for j in range(n):
            if matrix[i][j] == 1:
                deg += 1
        m.append(deg)
    for j in m:
        if j == 1:
            res += 1
    print(res)


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        n = int(lines[0])
        matrix = []
        for line in lines[1:n+1]:
            m = list(map(int, line.strip().split()))
            matrix.append(m)
    solve(n, matrix)