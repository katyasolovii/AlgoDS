def bubble_sort(array):
    n = len(array)
    for j in range(n - 1, 0, -1):
        for i in range(j): 
            if array[i] > array[i + 1]: 
                array[i], array[i + 1] = array[i + 1], array[i]
    return array

if __name__ == '__main__':
    n = int(input())
    array = []
    for i in range(n):
        word = input()
        array.append(word)
    sorted_arr = bubble_sort(array)  
    for i in sorted_arr:
        print(i)
