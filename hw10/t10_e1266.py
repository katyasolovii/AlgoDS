def solve(lst, current_sum, N, j, possible_sums):
    if current_sum > N:
        return
    if current_sum in possible_sums:  
        return
    possible_sums.add(current_sum)

    for i in range(j, len(lst)):
        new_index = i + 1
        new_sum = current_sum + lst[i]
        solve(lst, new_sum, N, new_index, possible_sums)


if __name__ == "__main__":
    with open("input2.txt") as f:
        for line in f:
            numbers = list(map(int, line.split()))
            N = numbers[0]
            array = numbers[2:]
            possible_sums = set()
            solve(array, 0, N, 0, possible_sums)
            print(f"sum:{max(possible_sums)}")
