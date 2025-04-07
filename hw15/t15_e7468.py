class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None
        self.prev: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def ReorderList(self) -> None:
        """Перегрупувати елементи списку як наведено вище"""
        head_el = self.head
        tail_el = self.tail
        while head_el and tail_el and head_el != tail_el:
            if head_el:
                print(head_el.data, end=" ")
                head_el = head_el.next
            if head_el != tail_el:
                print(tail_el.data, end=" ")
                tail_el = tail_el.prev   
        if head_el == tail_el:
            print(head_el.data, end=" ")
        print()

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()


if __name__ == '__main__':
    lst = List()
    with open("input.txt") as f:
        lst_nums = list(map(int, f.read().split()))
        n = lst_nums[0]
        for i in range(n):
            lst.addToTail(lst_nums[i + 1])
    lst.ReorderList()