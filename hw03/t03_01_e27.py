def cyclic_shifts(n):
    length = len(bin(n)[2:])
    res = n

    for i in range(length - 1):
        # step_one = n << 1   
        # step_two = (1 << length) - 1
        # step_three = step_one  & step_two
        # step_four = n >> (length - 1)  
        new = ((n << 1) & ((1 << length) - 1)) | (n >> (length - 1)) 
        if new > res:
            res = new
        n = new
    return res

n = int(input())
print(cyclic_shifts(n))