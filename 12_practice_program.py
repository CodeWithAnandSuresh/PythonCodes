# Method1: Finding the length of the list using len function
# ==========================================================

# Gathering the list of values from the user

user_input = list(input("Enter the list of values: ").split(" "))

#Printing the length of the list using in-built len function

print(f"The length of the given list is: {len(user_input)}")


# Method2: Finding the length of the list without using any built-in function
# ============================================================================
# Initializing the length value as zero and gathering the list of values from the user

length = 0
user_input = list(input("Enter the list of values: ").split(" "))

# Looping through each element in the list and adding the count to the length variable

for i in user_input:
    length += 1

##Printing the length of the list

print(f"The length of the given list is: {length}")
