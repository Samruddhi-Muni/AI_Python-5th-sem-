# 5. (a) Write a python program to implement a function that counts the number of times a string (s1) occurs in another string(s2). 
 
def count_occurrences(main_string, substring):  
    count = 0 
    start_index = 0 
    while start_index < len(main_string):  
        index = main_string.find(substring, start_index)  
        if index == -1:  
            break 
        count += 1 
        start_index = index + 1  
    return count 
 
# Example usage: 
main_string = input("Enter the Main String: ")  
substring = input("Enter the Sub String: ") 
result = count_occurrences(main_string, substring) 
 
print(f"The substring '{substring}' occurs {result} times in the main string.")  
print(main_string.count(substring))
