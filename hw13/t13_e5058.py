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
    
    def empty(self):
        return self._top == -1

BRACKETS = {"(": ")", "[": "]", "{": "}"}

def check(sequence):
    s = Stack()
    for i in sequence:
        if i in BRACKETS:
            s.push(i)
        else:
            if s.empty() or BRACKETS[s.pop()] != i:
                return False
    return s.empty()

if __name__ == '__main__':
    with open("input.txt") as f:
        s = f.readline().rstrip()
        print("yes" if check(s) else "no")
