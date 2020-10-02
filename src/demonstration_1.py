"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""
def two_sum(nums, target):
    # Your code here
    for i_one in range(len(nums)):
        for i_two in range(i_one, len(nums)):
            sum = nums[i_one] + nums[i_two]
            if sum == target:
                return [i_one, i_two]

result = two_sum([3, 8, 12, 17], 15)
print(result)