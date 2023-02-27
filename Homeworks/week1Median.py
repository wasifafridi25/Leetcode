print("Please enter 3 numbers: ")
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
median = a 
if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
        
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 
print("The median is: ", median)






    
        

