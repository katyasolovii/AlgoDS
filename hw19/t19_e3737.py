class Heap:
    
    def __init__(self):
        self._items = []

    def is_heap(self, n):
        for i in range(1, n + 1):
            left = 2 * i
            right = 2 * i + 1

            if left <= n and self._items[i - 1] > self._items[left - 1]: 
                return False
            if right <= n and self._items[i - 1] > self._items[right - 1]: 
                return False
        return True


if __name__ == '__main__':
    with open("input.txt") as f:
        heap = Heap()
        lines = f.readlines()
        n = int(lines[0])
        heap._items = list(map(int, lines[1].split()))
        
        if heap.is_heap(n):
            print("YES")
        else:
            print("NO")
