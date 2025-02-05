import math

def f(x):
    return x**2 + math.sqrt(x)

def condition(m, l, r):
    return l != m and r != m

def find_x(f, c):
    l = 0
    r = 10**10
    m = (l + r) / 2.0
    
    while condition(m, l, r):
        if f(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0
    return m

c = float(input())
print(f"{find_x(f, c):.6f}")
