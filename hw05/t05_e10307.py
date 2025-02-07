def binary_search(intervals, cows):
    left = 1
    right = max(max(intervals))
    d = 1

    while left <= right:
        m = (left + right) // 2
        if place_cows(intervals, cows, m):
            d = m
            left = m + 1
        else:
            right = m - 1
    return d

def place_cows(intervals, n, d):
    cows_placed = 1
    postion = intervals[0][0] 
    
    for a, b in intervals:
        p = max(postion + d, a) 
        while p <= b: 
            cows_placed += 1 
            postion = p 
            p += d  
            if cows_placed == n: 
                return True
    return False

if __name__ == '__main__':
    f = open("input.txt")

    number_cows, amount_grass  = [int(x) for x in f.readline().split()]
    array_intervals = []
    for i in range(amount_grass):
        interval = [int(x) for x in f.readline().split()]
        array_intervals.append(interval)
    f.close()
    array_intervals.sort()
    print(binary_search(array_intervals, number_cows)) 

# number_cows = 5
# array_intervals = [[0, 2], [4, 7], [9, 9]]
# array_intervals.sort()
# print(binary_search(array_intervals, number_cows)) 