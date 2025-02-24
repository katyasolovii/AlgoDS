import math

EMPTY = None


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Set:

    M = 31

    def __init__(self, size=1000003):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | str] = [EMPTY for _ in range(size)]

    def rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2
        
        _keys = self._keys
        self.__init__(self._size)
        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                self.add(_keys[i])

    def hash(self, s):
        h = 0
        for i in range(len(s)):
            h = h * self.M + ord(s[i])
        return h % self._size

    def add(self, key: str):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return
            i = (i + 1) % self._size

        self._count += 1
        self._keys[i] = key

    def __len__(self):
        return self._count
    
    def __contains__(self, key):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return True
            i = (i + 1) % self._size
        return False
        
    def same_words(self, other):
        for word in self._keys:
            if word is not EMPTY and word not in other:
                return False
        return True


if __name__ == '__main__':
    N, M = map(int, input().split())
    words = Set()

    for _ in range(N):
        words.add(input().strip().lower())

    text = Set()
    for _ in range(M):
        line = input().strip().lower()
        temp = ""
        for j in line:
            if j.isalpha():
                temp += j
            else:
                if temp: 
                    text.add(temp)
                    temp = ""
        if temp:
            text.add(temp)

    if len(text) == len(words):
        print("Everything is going to be OK.")
    elif not text.same_words(words):
        print("Some words from the text are unknown.")
    else:
        print("The usage of the vocabulary is not perfect.")
