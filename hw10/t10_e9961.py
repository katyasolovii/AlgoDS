def sequences(lst: list, k: int, n: int):
    if len(lst) == k:
        print(*lst)
        return  
    
    for i in range(1, n + 1):
        if i not in lst:
            lst_next = lst[:]
            lst_next.append(i)
            sequences(lst_next, k, n)    


if __name__ == '__main__':
    f = open("input1.txt")
    for line in f:
        n, k = map(int, line.split())
        lst = []
        sequences(lst, k, n)
    f.close()