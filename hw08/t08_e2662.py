def selection_sort(array):
    n = len(array)
    element = array[0]
    index = 0
    count = 0
    for j in range(0, n):
        pos = j
        for i in range(pos + 1, n):
            if array[i] < array[pos]:
                pos = i  
        if pos != j:   
            array[j], array[pos] = array[pos], array[j]
            if index != array.index(element):
                count += 1
                index = array.index(element)
    print(count)

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    selection_sort(array)