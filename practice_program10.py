# Prompt the user to enter values separated by spaces
user_input = input("Enter the values: ").split()

# Print the original list
print("Original list:", user_input)

# Swap the first and last elements
first_element = user_input[0]
last_element = user_input[-1]
user_input[0] = last_element
user_input[-1] = first_element

# Print the modified list
print("Swapped list:", user_input)
