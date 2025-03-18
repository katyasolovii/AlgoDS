class Stack:

    def __init__(self, maxsize=1000):
        self._items = [0 for _ in range(maxsize)]
        self._top = -1

    def push(self, item):
        self._top += 1
        self._items[self._top] = item

    def pop(self):
        item = self._items[self._top]
        self._top -= 1
        return item

    def size(self):
        return self._top + 1

    def back(self):
        return self._items[self._top]


def solve(data):
    i = 0
    res = []
    while len(data) > i:
        if data[i] == "0":
            break
        n = int(data[i])
        i += 1
        while data[i] != "0":
            m = list(map(int, data[i].split()))
            i += 1
            curr = 1
            stack = Stack()
            t_f = True
            for k in m:
                while curr <= n:
                    if stack.back() != k:
                        stack.push(curr)
                        curr += 1
                    else:
                        break
                # print(stack.back())
                if stack.back() == k:
                    stack.pop()
                else:
                    t_f = False
                    break
            if t_f:
                res.append("Yes")
            else:
                res.append("No")
        res.append("") 
        i += 1
    print("\n".join(res))


if __name__ == '__main__':
    with open("input.txt") as f:
        data = []
        for line in f:
            data.append(line.strip())
    solve(data)