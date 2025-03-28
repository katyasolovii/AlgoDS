class Node:
    def __init__(self, item):
        self.item = item    
        self.next = None


class Stack:
    def __init__(self, maxsize=100):
        self._top = None
        self._size = 0  
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
        return "ok"

    def exit(self):
        return "bye"
    
    def size(self):
        return self._size
    
    def empty(self):
        return self._top is None
    
    def pop(self):
        if self._top is None:
            return "error"
        else:
            item = self._top.item 
            self._top = self._top.next 
            self._size -= 1
            return item
        
    def clear(self):
        self._top = None
        self._size = 0
        return "ok"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)

    def back(self):
        if self._top is None:
            return "error"
        return self._top.item
    

if __name__ == '__main__':
    stack = Stack()
    with open("input.txt") as f:
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break