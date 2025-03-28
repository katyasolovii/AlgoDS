def convert(number: str, to_base: int):
    stack = []
    num = int(number)
    while num != 0:
        d = num % to_base
        num = num // to_base
        stack.append(d)
    res = ''
    while stack:
        n = stack.pop()
        if n < 10:
            res += str(n)
        else:
            res += f'[{n}]'
    print(res)

if __name__ == '__main__':
    with open("input.txt") as f:
        n = f.readline().strip()
        base = int(f.readline().strip())
    convert(n, base)