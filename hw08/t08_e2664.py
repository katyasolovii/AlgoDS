def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        pos = i
        x = array[pos]
        while pos > 0:
            if array[pos - 1] > x:
                array[pos] = array[pos - 1]
                pos -= 1
            else:
                break
        array[pos] = x
        if pos != i:
            print(*array)
         

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    insert_sort(array)
