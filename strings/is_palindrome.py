# Problem: Valid Palindrome
# Given a string s, return True if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
# Because after removing non-alphanumeric characters and making it lowercase → "amanaplanacanalpanama" is a palindrome

# Example 2:
# Input: s = "race a car"
# Output: False

# Edge Case:
# Input: s = ""
# Output: True

# Constraints:
# You may assume s contains only printable ASCII characters.

# Time & Space Complexity:
# Time: O(n)
# Space: O(n)

def is_palindrome(input_string):
  merged_string = ''.join(ch.lower() for ch in input_string if ch.isalnum())
  return merged_string == merged_string[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
print(is_palindrome(""))                                # True
print(is_palindrome("0P"))                              # False
print(is_palindrome("madam"))                           # True
