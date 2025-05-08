# Problem: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Example:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Because nums[0] + nums[1] == 2 + 7 == 9

# Constraints:
# Only one valid answer exists.
# Same element cannot be used twice.
# Return the indices (not values).
# Time complexity matters: Try to do better than brute force.

# Time & Space:
# Time: O(n)
# Space: O(n)

def two_sum_hashmap(nums, target):
    num_to_index = {}  # key: number, value: index

    for i, num in enumerate(nums):
        remainder = target - num
        if remainder in num_to_index:
            return [num_to_index[remainder], i]
        num_to_index[num] = i  # store number seen so far with index
    
    return []

# Example usage
print(two_sum_hashmap([2, 11, 7, 15], 9))  # Expected: [0, 1]