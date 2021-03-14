"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""

"""
def nth_smallest(lst, n):
    # Your code here
    lst.sort()
    return lst[n-1]  #because numbers in python always starts @ 0

print(nth_smallest([7, 3, 5, 1], 2))  #3




"""

def nth_smallest(lst, n):
    if n > len(lst):
        return None  #if error return it None
    # Your code here
    lst.sort()
    return lst[n - 1]

print(nth_smallest([7, 3, 5, 1], 2))  #3
print(nth_smallest([1, 3, 5, 7], 5))  #None