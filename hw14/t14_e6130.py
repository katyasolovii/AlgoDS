class Node:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None 

class Deque:

    def __init__(self):
        self._front_node = None
        self._back = None
        self._size = 0

    def push_front(self, item):
        new_node = Node(item)
        if self._front_node is None:
            self._front_node = self._back = new_node
        else:
            new_node.next = self._front_node
            self._front_node.prev = new_node
            self._front_node = new_node
        self._size += 1
        return "ok"

    def push_back(self, item):
        new_node = Node(item)
        if self._back is None:
            self._front_node = self._back = new_node
        else:
            new_node.prev = self._back
            self._back.next = new_node
            self._back = new_node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._front_node is None:
            return "error"
        value = self._front_node.item
        self._front_node = self._front_node.next
        if self._front_node is None:
            self._back = None
        else:
            self._front_node.prev = None
        self._size -= 1
        return value

    def pop_back(self):
        if self._back is None:
            return "error"
        value = self._back.item
        self._back = self._back.prev
        if self._back is None:
            self._front_node = None
        else:
            self._back.next = None
        self._size -= 1
        return value

    def front(self):
        if self._front_node is None:
            return "error"
        return self._front_node.item

    def back(self):
        if self._back is None:
            return "error"
        return self._back.item

    def size(self):
        return self._size

    def clear(self):
        self._front_node = self._back = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.strip().split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    deque = Deque()
    with open("input.txt") as f:
        for line in f:
            res = deque.execute(line)
            print(res)
            if res == "bye":
                break
