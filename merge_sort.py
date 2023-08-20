arr = [55, 11, 76, 20, 3, 2, 1]

def merge_sort(arr):
    if (len(arr)) > 1:
        # midpoint of array
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        merge_sort(left)
        merge_sort(right)

        i = 0 # left index
        j = 0 # right index
        k = 0 # arr index

        while (i < len(left)) and (j < len(right)):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

print(arr)
merge_sort(arr)
print(arr)

