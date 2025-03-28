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

def is_correct(s):
    stack = Stack(len(s))
    for i in s:
        if i == ")":
            if stack.empty() or stack.pop() != "(":
                return False
        elif i == "]":
            if stack.empty() or stack.pop() != "[":
                return False    
        else:
            stack.push(i)
    return stack.empty()    

def generate(curr_line, open1, close1, open2, close2, n):
    if len(curr_line) == n:
        if is_correct(curr_line): 
            print(curr_line)
        return
    
    if open1 < n:
        generate(curr_line + "(", open1 + 1, close1, open2, close2, n)
    if open2 < n:
        generate(curr_line + "[", open1, close1, open2 + 1, close2, n)
    if close1 < open1:
        generate(curr_line + ")", open1, close1 + 1, open2, close2, n)
    if close2 < open2:
        generate(curr_line + "]", open1, close1, open2, close2 + 1, n)

if __name__ == '__main__':
    n = int(input())  
    generate("", 0, 0, 0, 0, n) 
