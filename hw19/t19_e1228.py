class Heap:

    def __init__(self):
        self._items = [0]

    def _swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def insert(self, item):
        self._items.append(item)
        self._sift_up()

    def extract_min(self):
        self._swap(1, -1)
        item = self._items.pop() 
        self._sift_down()
        return item

    def _sift_up(self):
        i = len(self._items) - 1
        while i > 1:
            parent = i // 2
            if self._items[i] >= self._items[parent]:
                break
            self._swap(i, parent)
            i = parent

    def _sift_down(self):
        i = 1
        while i * 2 < len(self._items):
            left = i * 2
            right = left + 1
            if right < len(self._items) and self._items[left] > self._items[right]:
                min_child = right
            else:
                min_child = left

            if self._items[min_child] >= self._items[i]:
                break

            self._swap(min_child, i)
            i = min_child
            
    def size(self):
        return len(self._items) - 1 

if __name__ == '__main__':
    with open("input.txt") as f:
        heap = Heap()
        lines = f.readlines()
        n = int(lines[0])  
        arr = list(map(int, lines[1].split()))

        for el in arr:
            heap.insert(el)

        res = 0
        while heap.size() > 1:
            value = heap.extract_min() + heap.extract_min()
            res += value
            heap.insert(value)
        print(res)
