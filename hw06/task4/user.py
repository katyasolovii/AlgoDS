
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class Node:
# прямокутник зі стрілкою
    def __init__(self, author: str, title: str):
        self.author: str = author
        self.title: str = title
        self.next: [None | Node] = None


size: int = 10_000
slots: list[None | Node]


def __hash__(value: str):
    return hash(value) % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots
    slots = [None for _ in range(size)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    i = __hash__(author)
    slot = slots[i]
    while slot is not None:
        if slot.author == author and slot.title == title:
            return 
        slot = slot.next

    node = Node(author, title)
    node.next = slots[i]
    slots[i] = node


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    i = __hash__(author)
    node = slots[i]
    while node is not None:
        if node.author == author and node.title == title:
            return True
        node = node.next
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    i = __hash__(author)
    node = slots[i]
    if node is None:
        return
    if node.author == author and node.title == title:
        slots[i] = node.next
        return
    
    prev = node
    node = node.next
    while node is not None:
        if node.author == author and node.title == title:
            prev.next = node.next
            return
        prev = node
        node = node.next


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    books = []
    i = __hash__(author)
    node = slots[i]
    while node is not None:
        if node.author == author:
            books.append(node.title)
        node = node.next
    return books
