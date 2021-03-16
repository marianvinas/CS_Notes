"""
Constant Time 0(1)
"""

def print_one_item(items):
    print(item[0])

"""
Linear Time 0(n)
"""

def print_every_time(items):
    for item in items:
        print(item)

"""
Quadratic time 0(n^2)
"""
def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)

"""
Classify the runtime complexity of the
number_of-steps function below using Big O notation.
"""
def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps

"""
Linear Space O(n)
"""
def append_to_list_n_times(n):
    my_list = []

    for _ in range(n):
        my_list.append("Lambda")

    return my_list
