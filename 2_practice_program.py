"""
Finds the missing number in an array of integers from 1 to n.
Args:
  arr (list): List of integers from 1 to n with one number missing.
Returns:
  int: The missing number in the array.
"""

def find_missing_number(arr):
    n = len(arr) + 1  # Total number of elements, including the missing number
    arr_sum = sum(arr)  # Sum of all elements in the array
    expected_sum = (n * (n + 1)) // 2  # Sum of all numbers from 1 to n
    missing_number = expected_sum - arr_sum  # Calculate the missing number
    return missing_number

# Example usage
arr_input = input("Enter the array of integers (space-separated): ")
arr = list(map(int, arr_input.split()))

missing_number = find_missing_number(arr)
print("The missing number is:", missing_number)
