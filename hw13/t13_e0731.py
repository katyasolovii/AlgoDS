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

OPERANDS = "+-*/"

def solve(s):
    stack = Stack()
    inverse_s = s[::-1] 
    for i in inverse_s:
        if i in OPERANDS: 
            left, left_operand = stack.pop()
            right, right_operand = stack.pop()

            if i == "+":
                stack.push((left + i + right, i))
            elif i == "-":
                if right_operand == "+" or right_operand == "-":
                    right = "(" + right + ")"
                stack.push((left + i + right, i))
            elif i == "*":
                if left_operand == "+" or left_operand == "-":
                    left = "(" + left + ")"
                if right_operand == "+" or right_operand == "-":
                    right = "(" + right + ")"
                stack.push((left + i + right, i))
            elif i == "/":
                if left_operand == "+" or left_operand == "-":
                    left = "(" + left + ")"
                if right_operand != "":
                    right = "(" + right + ")"
                stack.push((left + i + right, i))
            else:
                stack.push((left + i + right, i))
        else:  
            stack.push((i, ""))
    return stack.pop()[0]
                 

if __name__ == "__main__":
    s = input()
    print(solve(s))
    