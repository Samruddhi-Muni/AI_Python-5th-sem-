#PART-A
# 1. (C)Write a python program to find factorial of the given number? 
 
num=int(input('enter the number :'))
fact=1 
for i in range(1,num+1):  
    fact=fact*i 
print(f"The Factorial of {num} is:",fact)
