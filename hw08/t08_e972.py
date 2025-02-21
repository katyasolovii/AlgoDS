def bubble_sort(array):
    n = len(array)
    for j in range(n - 1, 0, -1):
        for i in range(j): 
            if array[i] > array[i + 1]: 
                array[i], array[i + 1] = array[i + 1], array[i]
    return array

if __name__ == '__main__':
    n = int(input()) 
    data = [] 

    for _ in range(n):
        line = input()  
        data.append(list(map(int, line.split()))) 

    sorted_res = bubble_sort(data)
    for i in sorted_res:
        print(*i)