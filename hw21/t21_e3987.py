def solve(n, edges):
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) not in edges:
                print("NO")
                return

    print("YES")


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.readlines()
        n, m = map(int, lines[0].split())
        edges = []
        for i in range(1, 1 + m):
            k = lines[i].split()
            u = int(k[0])
            v = int(k[1])
            edges.append((u, v))
    solve(n, edges)