"""
Python – Swap elements in String list

Input: ['Gfg', 'is', 'best', 'for', 'Geeks']
Output: ['efg', 'is', 'bGst', 'for', 'eGGks']

"""

# Time Complexity: O(n)

def swapElements(inputlist:list,char1:str,char2:str):
    result = [sub.replace(char1,'-').replace('e','G').replace('-','e') for sub in inputlist]
    return result

print("The list after swaping the elements are: ",swapElements(['Gfg', 'is', 'best', 'for', 'Geeks'],'G','e'))

# Output: The list after swap is:  ['efg', 'is', 'bGst', 'for', 'eGGks']
