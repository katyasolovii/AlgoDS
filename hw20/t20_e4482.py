import math


class SegmentTree:

    def __init__(self, array):
        k = len(array)
        n = 1 << math.ceil(math.log2(k))
        self.tree_gcd = [0] * (2 * n)
        self.tree_lcm = [1] * (2 * n)
        self.size = n

        for i in range(k):
            self.tree_gcd[n + i] = array[i]
            self.tree_lcm[n + i] = array[i]
        for i in range(n - 1, 0, -1):
            self.tree_gcd[i] = math.gcd(self.tree_gcd[2 * i], self.tree_gcd[2 * i + 1])
            self.tree_lcm[i] = math.lcm(self.tree_lcm[2 * i], self.tree_lcm[2 * i + 1])

    def gcd_search(self, left, right):
        left += self.size
        right += self.size
        res = 0
        while left <= right:
            if left % 2 == 1:
                res = math.gcd(res, self.tree_gcd[left])
                left += 1
            if right % 2 == 0:
                res = math.gcd(res, self.tree_gcd[right])
                right -= 1
            left //= 2
            right //= 2
        return res

    def lcm_search(self, left, right):
        left += self.size
        right += self.size
        res = 1
        while left <= right:
            if left % 2 == 1:
                res = math.lcm(res, self.tree_lcm[left])
                left += 1
            if right % 2 == 0:
                res = math.lcm(res, self.tree_lcm[right])
                right -= 1
            left //= 2
            right //= 2
        return res

    def update(self, i, x):
        i += self.size
        self.tree_gcd[i] = x
        self.tree_lcm[i] = x
        i //= 2
        while i >= 1:
            self.tree_gcd[i] = math.gcd(self.tree_gcd[2 * i], self.tree_gcd[2 * i + 1])
            self.tree_lcm[i] = math.lcm(self.tree_lcm[2 * i], self.tree_lcm[2 * i + 1])
            i //= 2


if __name__ == '__main__':
    n = int(input())  
    arr = list(map(int, input().split()))  
    m = int(input()) 
    tree = SegmentTree(arr)
    
    for _ in range(m):
        q, l, r = map(int, input().split()) 
        if q == 1:
            gcd = tree.gcd_search(l - 1, r - 1) 
            lcm = tree.lcm_search(l - 1, r - 1)  
            if gcd < lcm:
                print("wins")
            elif gcd > lcm:
                print("loser")
            else:
                print("draw")
        elif q == 2:
            tree.update(l - 1, r) 