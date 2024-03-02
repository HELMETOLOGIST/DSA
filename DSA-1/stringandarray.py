#### Count the longest substring in this String
s = "aabcdaaabbbbbbbbbbbbbbbacaaaaaabbaaaaaaaaaaaacaaadgdaaalmaaaaaa"
max_count = 0
max_string = ''
count = 0
first = s[0]
sub_string = ''
for i in range(len(s)):
    
    if  s[i] == first:
        sub_string += s[i]
        count += 1

    elif s[i] != first:
        if count > max_count:
            max_count = count 
            max_string = sub_string
        count = 1
        first = s[i]
        sub_string = s[i]
   
print(max_string)

#### Count a the 2 equal substring in a string
s = "aabcdaaabbbbbbbbbbacaaaaaabbaaaaaaaaaaaacaaadgdaaalmaaaaaa"
a_count = 0
count = 0
for i in range(len(s)):
   
    if s[i]=='a':
        count +=1
    if s[i] != 'a':
        if count == 2:
            a_count += 1
        count = 0  
    if count == 2 and i == len(s)-1:
        a_count += 1    
print(a_count)   