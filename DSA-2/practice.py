def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [45,39,87,45,33,74]
bubble_sort(arr)
print(arr)


def bubble_sort_sl(arr):
    for i in range(2):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [7,65,42,34,59,8,5]
bubble_sort(arr)
print(arr[-2])


def bubble_sorted_or_not(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break

arr = [1,2,3,4,53,6,7,8,9]
bubble_sorted_or_not(arr)
print(arr)
