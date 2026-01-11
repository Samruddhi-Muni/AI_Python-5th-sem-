# 2. (a) Write a python program to implement List operations (Nested List, Length, Concatenation, Membership, Iteration, Indexing and Slicing). 

# Nested List 
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
print(list) 
 
#Length of the List 
length=len(list) 
print('length of the list',length) 
 
# Concatenation of Lists 
list1 = [1, 2, 3] 
list2 = [4, 5, 6] 
concatenated_list = list1 + list2 
print(concatenated_list) 
 
# Membership Check 
print(2 in list1) 
print(3 not in list2) 
 
# Iterate over a list 
for i in list1: 
    print(i) 
  
fruits = ['apple', 'banana', 'cherry'] 
 
x = fruits.index("apple") 
 
print(x) 
 
# Slicing
List = [50, 70, 30, 20, 90, 10, 50] 
# Display list 
print(List[1:5])
