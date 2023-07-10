# Prompt the user to enter a list of values separated by spaces

user_input = list(input("Enter the list of values: ").split(" "))

# Prompt the user to enter the positions of the values to be swapped

first_position = int(input("Enter the position of the first value to be swapped: "))
second_position = int(input("Enter the position of the second value to be swapped: "))

# Swapping the values in the list based on the positions entered

user_input[first_position - 1], user_input[second_position - 1] = user_input[second_position - 1], user_input[first_position - 1]

# Printing the swapped list of values

print(f"The swapped list of values is: {user_input}")
