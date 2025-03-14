def karatsuba(x, y):
    max_len = max(len(str(x)), len(str(y)))

    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    
    half_max = max_len // 2
    
    B = 10 ** half_max

    left_x = x // B
    right_x = x % B
    left_y = y // B
    right_y = y % B

    sum_x = int(left_x) + int(right_x)
    sum_y = int(left_y) + int(right_y)

    z0 = karatsuba(left_x, left_y)
    z1 = karatsuba(right_x, right_y)
    z2 = karatsuba(sum_x, sum_y)

    return int(z0) * 10**(2*half_max) + (int(z2) - int(z0) - int(z1)) * B + int(z1)


if __name__ == '__main__':
    with open("input.txt") as f:
        x, y = map(int, f.readline().split())
    print(karatsuba(x, y))
