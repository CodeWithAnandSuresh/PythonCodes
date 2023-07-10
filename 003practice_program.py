"""
 Remove Duplicates: 
 
 Write a function to remove duplicates from a list without using any built-in functions or external data structures.
 
 """

values = []
usr_input = input("Enter the values: ")
input_list = usr_input.split()

for i in input_list:
    if i not in values:
        values.append(i)

unique_values = " ".join(values)
print("Unique values:", unique_values)
