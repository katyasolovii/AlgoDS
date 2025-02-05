import math

def f(x):
    return math.sin(x) - x / 3.0

def condition(m, l, r):
    return l != m and r != m

def solve(f, c, a, b):
    left = a
    right = b
    m = (left + right) / 2.0
    while left != m and right != m:
        if f(m) > c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0
    return m

print(solve(f, 0, 1.6, 3.0)) #res: 2.278862660075828
 