class Heap:
    def __init__(self):
        self._items = [0]
        self._positions = {} 

    def _swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]
        self._positions[self._items[i][1]] = i
        self._positions[self._items[j][1]] = j

    def insert(self, id, priority):
        self._items.append((priority, id))
        self._positions[id] = len(self._items) - 1
        self._sift_up()

    def _sift_up(self):
        i = len(self._items) - 1
        while i > 1:
            parent = i // 2
            if self._items[i][0] <= self._items[parent][0]:
                break
            self._swap(i, parent)
            i = parent

    def extract_max(self):
        self._swap(1, - 1)
        max_item = self._items.pop()
        self._positions[max_item[1]] = 0
        self._sift_down()
        return max_item[1], max_item[0] 

    def _sift_down(self):
        i = 1
        while i * 2 < len(self._items):
            left = i * 2
            right = left + 1
            max_child = left
            if right < len(self._items) and self._items[left][0] > self._items[right][0]:
                max_child = right
            else:
                max_child = left

            if self._items[i][0] >= self._items[max_child][0]:
                break

            self._swap(i, max_child)
            i = max_child

    def change_priority(self, id, new_priority):
        index = self._positions[id]
        prev_priority, _ = self._items[index]
        self._items[index] = (new_priority, id)
        if new_priority > prev_priority:
            self._sift_up()
        else:
            self._sift_down()

if __name__ == '__main__':
    heap = Heap()
    with open("input.txt") as f:
        for line in f:
            data = line.strip().split()
            if not data:
                continue
            cmd = data[0]
            if cmd == 'ADD':
                id = data[1]
                priority = int(data[2])
                heap.insert(id, priority)
            elif cmd == 'POP':
                id, priority = heap.extract_max()
                print(f"{id} {priority}")
            elif cmd == 'CHANGE': 
                id = data[1]
                new_priority = int(data[2])
                heap.change_priority(id, new_priority)
