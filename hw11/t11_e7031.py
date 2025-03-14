def count_inversions(lst, t):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j] + t:
                count += 1
    return count

def solve(lst, t):
    if len(lst) <= 1:
        return 0, lst  

    middle_lst = len(lst) // 2
    left_part = lst[:middle_lst]
    right_part = lst[middle_lst:]

    left_inv, left_sorted = solve(left_part, t)
    right_inv, right_sorted = solve(right_part, t)

    count = 0
    i = 0
    j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] > right_sorted[j] + t:
            count += len(left_sorted) - i  
            j += 1
        else:
            i += 1

    res = left_inv + right_inv + count  

    sorted_lst = []
    i = 0 
    j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            sorted_lst.append(left_sorted[i])
            i += 1
        else:
            sorted_lst.append(right_sorted[j])
            j += 1

    while i < len(left_sorted):
        sorted_lst.append(left_sorted[i])
        i += 1

    while j < len(right_sorted):
        sorted_lst.append(right_sorted[j])
        j += 1

    return res, sorted_lst

if __name__ == '__main__':
    n, t = map(int, input().split())  
    lst = list(map(int, input().split()))
    result, r_l = solve(lst, t)  
    print(result) 
