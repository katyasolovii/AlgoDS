def sorted(array, x, y):
    res = 0
    for i in array:
        if i >= x and i <= y:
            res += 1
    return res

if __name__ == '__main__':
    f = open("input2.txt")
    while f.readline():
        array1 = [int(x) for x in f.readline().split()]  
        x1, y1 = [int(x) for x in f.readline().split()]  
        print(sorted(array1, x1, y1))
    f.close()