import math

EMPTY = None

def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

class Phone_Book:

    def __init__(self, size=1000003):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | int] =  [EMPTY for _ in range(size)]

    def rehash(self, key: int):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

    def hash(self, key: int):
        return key % self._size
    
    def add(self, key: int):
        if self._size * 0.7 < self._count:
            self._rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return
            i = (i + 1) % self._size

        self._count += 1
        self._keys[i] = key

    def __len__(self):
        return self._count


if __name__ == '__main__':
    n = int(input())
    phone_numbers = [int(el) for el in input().split()]
    
    contacts = Phone_Book()
    
    for num in phone_numbers:
        contacts.add(num)
    
    print(len(contacts))
