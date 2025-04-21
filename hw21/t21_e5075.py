def solve(n, edges):
    in_degree = []
    out_degree = []

    for i in range(1, n + 1):
        r_1 = 0 
        r_2 = 0 
        for u, v in edges:
            if u == i:
                r_1 += 1
            if v == i:
                r_2 += 1
        in_degree.append(r_2)
        out_degree.append(r_1)

    for i, j in zip(in_degree, out_degree):
        print(i, j)
        

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