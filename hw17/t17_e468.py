class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        node = self
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = SearchTree(key)
                    break
                else:
                    node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right
            else:
                break
    
    def exist_way(self, way):
        node = self
        index = 0

        while index < len(way):
            if node.key != way[index]:
                return False
            index += 1

            if index == len(way):
                if node.right is None and node.left is None:
                    return True

            if node.key > way[index]:
                if node.left is None:
                    return False
                node = node.left
            else:
                if node.right is None:
                    return False
                node = node.right
        return False


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline()
        way = [int(el) for el in line.split()]
        tree = SearchTree(way[0])
        for i in way[1:]:
            tree.insert(i)
        
        if tree.exist_way(way):
            print("YES")
        else:
            print("NO")
