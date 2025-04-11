class Tree:
    def __init__(self, key, data=0, parent=None):
        self.key = key
        self.data = data
        self.parent = parent
        self.children = []

    def add_children(self, children):
        self.children.append(children)

    def dfs(self, res_sum):
        if not self.children:
            return res_sum + self.data
        
        min_sum = 10_000
        for child in self.children:
            child_bribe = child.dfs(res_sum + self.data)
            min_sum = min(min_sum, child_bribe) 
        
        return min_sum

    def min_bribe(self):
        return self.dfs(0)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())
        nodes = {}

        for i in range(1, n + 1):
            nodes[i] = Tree(i) 

        for i in range(1, n + 1):
            line = list(map(int, f.readline().split())) 
            data = line[0]  
            count = line[1] 
            children = line[2:] 
            nodes[i].data = data  
            for child in children:  
                nodes[i].children.append(nodes[child])

        res = nodes[1].min_bribe()  
        print(res) 
