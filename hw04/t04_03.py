def f(x):
    return x**3 + x + 1

def condition(m, l, r):
    return l != m and r != m

def solve(f, c, a, b):
    left = a
    right = b
    m = (left + right) / 2.0
    
    while condition(m, left, right):
        if f(m) > c:
            right = m
        else:
            left = m
        m = (left + right) / 2.0
    return m 

print(solve(f, 5, 0, 10)) #res: 1.3787967001295511
 