"""
Q: Python Program to Swap Two Elements in a List

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]
"""

# Time Complexity: O(1)

def swapTwoElements(inputlist:list,pos1:int,pos2:int):
    inputlist[pos1-1],inputlist[pos2-1] = inputlist[pos2-1],inputlist[pos1-1]
    return inputlist
  
print("The list after swap is: ",swapTwoElements([23, 65, 19, 90],1,3))

# Output: The list after swap is:  [19, 65, 23, 90]
