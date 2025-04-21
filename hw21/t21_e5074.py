def solve(n, edges):
    m = set()
    for u, v in edges:
        if (u, v) in m:
            print("YES") 
            return
        m.add((u, v))
    print("NO")

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