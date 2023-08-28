"""
Q: Python program to interchange first and last elements in a list

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""
# Time Complexity: O(1)
# ======================

def interChangeElements(inputlist:list):
    inputlist[0],inputlist[-1] = inputlist[-1],inputlist[0]
    return inputlist

print("The list after elements interchanged is: ",interChangeElements([12, 35, 9, 56, 24]))

# Output: The list after elements interchanged is:  [24, 35, 9, 56, 12]
