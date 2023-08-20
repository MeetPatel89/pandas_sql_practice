def find_missing_num(arr):
    n = len(arr)
    for i in range(n):
        if i not in arr:
            return i

def find_missing_num_2(arr):
    n = len(arr) + 1
    expected_sum = int(n*(n-1)/2)
    return expected_sum - sum(arr)

arr = [0,1,2,4,5] 
print(find_missing_num(arr))
print(find_missing_num_2(arr))