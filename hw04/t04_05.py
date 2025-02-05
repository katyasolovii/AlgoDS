def f(x):
    return x**3 + 4*x**2 + x - 6

def condition(m, l, r):
    return l != m and r != m

def solve(f, a, b):
    left = a
    right = b
    m = (left + right) / 2.0
    
    while condition(m, left, right):
        if f(m) > 0:
            right = m
        else:
            left = m
        m = (left + right) / 2.0
    return m

print(solve(f, 0, 2)) #res: 1.0

