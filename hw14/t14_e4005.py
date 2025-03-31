class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self._front_node = None
        self._back = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        self._size += 1
        if self._size == 1:
            self._front_node = new_node
        else:
            self._back.next = new_node
        self._back = new_node

    def size(self):
        return self._size
    
    def front(self):
        if self._size == 0:
            return "error"
        return self._front_node.item

    def pop(self):
        if self._size == 0:
            return "error"
        current_front = self._front_node
        item = current_front.item
        self._size -= 1
        self._front_node = self._front_node.next
        del current_front
        if self._front_node is None:
            self._back = None
        return item

    def clear(self):
        self._size = 0
        self._front_node = self._back = None

MAX_MOVES = 200000

def solve(all_cards, player1, player2):
    f_queue = Queue()
    s_queue = Queue()
    
    for i in player1:
        f_queue.push(i)
    for i in player2:
        s_queue.push(i)
    
    all_moves = 0
    
    while f_queue.size() > 0 and s_queue.size() > 0:
        if all_moves >= MAX_MOVES:
            print("draw")
            return
        
        all_moves += 1
        first_card = f_queue.pop()
        second_card = s_queue.pop()
        
        if (first_card > second_card and not (first_card == n - 1 and second_card == 0)) or (first_card == 0 and second_card == n - 1):
            f_queue.push(first_card)
            f_queue.push(second_card)
        else:
            s_queue.push(first_card)
            s_queue.push(second_card)
    
    if f_queue.size() > 0:
        print("first", all_moves)
    else:
        print("second", all_moves)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())
        first_player = list(map(int, f.readline().strip().split()))
        second_player = list(map(int, f.readline().strip().split()))
    
    solve(n, first_player, second_player)
