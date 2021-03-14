"""
Challenge #8:

Create a function that returns the number of arguments it was called with.

Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""

# ...array
def num_args(*args, **kwargs):  #kwargs = keyword argument, spread any named arguments, 
    # Your code here
    print(len(args))  #2
    print(kwargs)     #{'arg2': 'this is a keyword arg'}
    return

num_args("foo", "bar", arg2='this is a keyword arg')
# num_args("foo")
