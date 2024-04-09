def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    

arr = [23, 12, 54, 11, 46, 72, 83, 33, 6]
qs = quick_sort(arr)
print(qs)

for i in arr[:-1]:
    print(i, end=', ')
print(54<46)