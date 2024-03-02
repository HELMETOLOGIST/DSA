#### Find factorial of a number
def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)
    
print(factorial(5))    


#### find the sum of elements in a list using recursion
def sum_of_element_list(list):
    if not list:
        return 0
    else:
        return list[0] + sum_of_element_list(list[1:])
    

list = [1,2,3,5,6,7,89]
    
print(sum(list))  
print(sum_of_element_list(list))

#### Find a sum of a number
def sum(n):               
    if n <= 1:
        return n   
    else:
        return n + sum(n-1)
    
print(sum(5))    

#### A Method for fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(3))     

#### Next method for fibonaci series
def fibanoci(n,a=0,b=1):
    if n >= 0:
        print(a, end=" ")
        return fibanoci(n-1, b, a+b)
    else:
        return ""
print(fibanoci(6))

#### Revese a string using recursion
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
    
s = "nibin"
print(reverse(s))


#### Palindrome checking using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
    
s = "nijith"
if is_palindrome(s):
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")

#### Find in a array it is flattend list or not then get the output as a single array
def flattend_list(arr):
    flatlist = []
    for i in arr:
        if isinstance(i,list):
            flatlist.extend(flattend_list(i))
        else:
            flatlist.append(i)
    return flatlist

arr = [1,[2,3],4,[5,[8,9]]]
flat = flattend_list(arr)
print(flat)