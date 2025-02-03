# bsearch_leftmost() з репозиторія Klevtsovskyi (task3 -> user.py)
def bsearch_leftmost(array, x):
    l = 0
    r = len(array)
    while l < r:
        m = l + (r - l) // 2
        if array[m] < x:
            l = m + 1
        else:
            r = m
    return l

def bsearch_rightmost(array, x):
    l = 0
    r = len(array)
    while l < r:
        m = l + (r - l) // 2
        if array[m] <= x:
            l = m + 1
        else:
            r = m
    return l 

if __name__ == '__main__':
    f = open("input1.txt")

    n = int(f.readline())  
    num_colors = [int(x) for x in f.readline().split()]  
    m = int(f.readline())  
    check_num = [int(x) for x in f.readline().split()]

    f.close()
    # n = 10
    # num_colors = [1, 1, 3, 3, 5, 7, 9, 18, 18, 57]
    # m = 5
    # check_num = [57, 3, 9, 1, 179]
    # print(bsearch_rightmost(num_colors, 1))
    for i in check_num:
        # останнє входження - перше входження
        print(bsearch_rightmost(num_colors, i) - bsearch_leftmost(num_colors, i))
