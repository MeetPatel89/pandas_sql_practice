def find_missing_num(n):
    curr_num = n[0]
    diff = 1
    missing_num = []
    for i, j in enumerate(n):
        if i != 0:
            diff = n[i] - curr_num
            if diff != 1:
                for k in range(diff-1):
                    missing_num.append(curr_num+(k+1))
        curr_num = n[i]
    return missing_num

arr = find_missing_num([0,1,2,4,7, 12])
print(arr)