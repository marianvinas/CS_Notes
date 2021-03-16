"""
Given an array of integers 'nums' and an integer 'target', return the indices
of two numbers that add up to the 'target'.

Examples:
- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:
- No negative numbers and no zero in array or target
- Return None if no answer
- Each input will have onle one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""

def two_sum(nums, target):
    num_dict = {}

    for i in range(len(nums)):
        num_dict[nums[i]] = i

    for i in range(len(nums)):
        current_num = nums[i]
        #check if the compliment is in dict
        compliment = target - current_num

        if compliment in num_dict:
            # compliment exists! return its index
            return [i, num_dict[compliment]]




    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         num1 = nums[i]
    #         num2 = nums[j]
    #         if num1 + num2 == target:
    #             return [i, j]

    # return None


print(two_sum(nums = [2,5,9,13], target = 7))  #[0, 1]
print(two_sum(nums = [4,3,5], target = 8))  #[1, 2]
#print(two_sum([8, 9, 13, 1, 14, 17, 14, 6, 8, 3, 2, 17, 1, 2, 12, 11, 3, 11, 3, 13, 14, 13, 14, 1, 9, 2, 13, 10, 10, 5, 3,], target = 12))