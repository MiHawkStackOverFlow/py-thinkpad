# Problem: Two Sum II – Input Array is Sorted (Easy-Medium)
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers added up to target, as a list [index1, index2] of 1-based indices.
# You must use only constant extra space.

# Example 1:
# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Because numbers[0] + numbers[1] = 2 + 7 = 9

# Example 2:
# Input: numbers = [2, 3, 4], target = 6
# Output: [1, 3]

# Example 3:
# Input: numbers = [-1, 0], target = -1
# Output: [1, 2]

# Constraints:
# You must use the fact that the array is sorted
# Only constant extra space allowed (O(1) space)
# Exactly one solution exists

# Final Complexity:
# Metric	Value	Reason
# Time	O(n)	Single pass from both ends
# Space	O(1)	No extra data structures used

def two_sum_sorted(numbers, target):
  left = 0
  right = len(numbers) - 1
  
  while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        return [left + 1, right + 1]
    elif current_sum < target:
        left += 1
    else:
        right -= 1

  return []


# Example usage
print(two_sum_sorted([2,7,11,15], 22))       # [2, 4]
print(two_sum_sorted([2, 3, 4], 6))          # [1, 3]
print(two_sum_sorted([-1, 0], -1))           # [1, 2]
print(two_sum_sorted([1, 2, 3, 4, 4, 9], 8)) # [4, 5]