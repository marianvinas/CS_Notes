"""
challenge #10

Create a function that applies a discount d to every number in the list.

Examples:
- get_discounts([2, 4, 6, 11], "50%") -> [1, 2, 3, 5.5]
- get_discounts([10, 20, 40, 80], "75%") -> [7.5, 15, 30, 60]
- get_discounts([100], "45%") -> [45]

Notes:
- The discount is the percentage of the original price(i.e the discount of
"75%" to 12 would be 9 as opposed to taking off 75% (making 3)).
- There won't be any awkward decimal numbers, only 0.5 to deal with.
"""
"""
def get_discounts(nums, percentage):
    # Your code here
    discount_percent = int(percentage[ :-1]) / 100
    new_nums = []
    for num in nums:
        #apply the discount
        new_nums.append(num * discount_percent)
    return new_nums

print(get_discounts([10, 20, 40, 80], "75%"))  #[7.5, 15.0, 30.0, 60.0]
------------------------------------
def get_discounts(nums, percentage):
    # Your code here
    discount_percent = int(percentage[ :-1]) / 100
    for i in range(0, len(nums)):
        #apply the discount
        nums[i] = nums[i] * discount_percent
    return nums

original_nums = [10, 20, 40, 80]

print(get_discounts(original_nums, "75%"))  #[7.5, 15.0, 30.0, 60.0]

print(original_nums)  #[7.5, 15.0, 30.0, 60.0]

"""

unique_number_var = 10

def add_num(num):
    num = num + 5
    return num

print(add_num(unique_number_var))  #15

print(unique_number_var) # 10
