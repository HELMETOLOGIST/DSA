def linear_search(arr,x):
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return-1
    
arr = [3,8,32,85,12,54]
x = 85
result = linear_search(arr,x)
print(result)