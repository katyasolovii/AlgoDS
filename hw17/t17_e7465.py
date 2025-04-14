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
                if node.right is None:
                    node.right = SearchTree(key)
                    break
                else:
                    node = node.right

    def print(self):
        if self.left is not None:
            self.left.print()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.print()
    
    def IsSameTree(self, other):
        if self.key != other.key:
            return False
        
        if self.left and other.left:
            if not self.left.IsSameTree(other.left):
                return False
        elif self.left or other.left:
            return False

        if self.right and other.right:
            if not self.right.IsSameTree(other.right):
                return False
        elif self.right or other.right: 
            return False

        return True

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        n = int(lines[0])
        list_1 = list(map(int, lines[1].split()))
        m = int(lines[2])
        list_2 = list(map(int, lines[3].split()))

        first_tree = SearchTree(list_1[0])
        second_tree = SearchTree(list_2[0])

        for i in list_1[1:]:
            first_tree.insert(i)
        for j in list_2[1:]:
            second_tree.insert(j)

        # first_tree.print()
        # print()  
        # second_tree.print()
        # print()

        if first_tree.IsSameTree(second_tree):
                print("1")
        else:
                print("0")