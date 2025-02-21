def bubble_sort(array):
    n = len(array)
    count = 0
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1
    print(count)

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    bubble_sort(array)