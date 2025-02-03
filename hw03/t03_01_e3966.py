def binary_search(array, x):
    left = 0
    right = len(array) - 1
    while left <= right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        elif array[m] > x:
            right = m - 1
        else:
            return True
    return False

if __name__ == '__main__':
    f = open("input.txt")

    n = int(f.readline())  
    num_butterfly = [int(x) for x in f.readline().split()]  
    m = int(f.readline())  
    check_num = [int(x) for x in f.readline().split()]

    f.close()

    for i in check_num:
        if binary_search(num_butterfly, i):
            print("YES")
        else:
            print("NO")
