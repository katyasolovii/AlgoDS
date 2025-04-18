import math


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        n = 1 << math.ceil(math.log2(k))
        self.tree = 2 * n * [0]
        self.size = n

        for i in range(k):
            self.tree[n + i] = array[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = math.gcd(self.tree[2 * i], self.tree[2 * i + 1])

    def gcd_search(self, left, right):
        left += self.size
        right += self.size

        res = 0
        while left <= right:
            if left % 2 == 1:
                res = math.gcd(res, self.tree[left])
                left += 1
            if right % 2 == 0:
                res = math.gcd(res, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return res

    def update(self, i, x):
        i += self.size
        self.tree[i] = x
        i = i // 2
        while i > 1:
            self.tree[i] = math.gcd(self.tree[2 * i], self.tree[2 * i + 1])
            i = i // 2


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    tree = SegmentTree(arr)
    for _ in range(m):
        q, l, r = map(int, input().split())
        if q == 1:
            print(tree.gcd_search(l - 1, r - 1))
        elif q == 2:
            tree.update(l - 1, r) 