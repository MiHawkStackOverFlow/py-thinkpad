# Problem: Valid Anagram
# Given two strings s and t,
# return True if t is an anagram of s, and False otherwise.

# Anagram Definition:
# An anagram is a word or phrase formed by rearranging the letters of another,
# using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: True

# Example 2:
# Input: s = "rat", t = "car"
# Output: False

# Edge Case:
# Input: s = "a", t = "a"
# Output: True

# Input: s = "a", t = "aa"
# Output: False

# Constraints:
# All letters are lowercase a–z
# Strings can be different lengths

# Time & Space Complexity:
# Time Complexity: O(n) — one pass through each string
# Space Complexity: O(1) — technically O(k) where k = 26 letters, but constant in practice

def is_anagram(string_one, string_two):
  string_map = {}

  if len(string_one) != len(string_two):
    return False

  for letter in string_one:
    string_map[letter] = string_map.get(letter, 0) + 1

  for letter in string_two:
    if letter in string_map:
      string_map[letter] -= 1
      if string_map[letter] == 0:
        del string_map[letter]
    else:
      # Letter not found or already zero
      return False

  return len(string_map) == 0

# Example usage
print(is_anagram("anagram", "nagaram"))   # True
print(is_anagram("rat", "car"))           # False
print(is_anagram("a", "a"))               # True
print(is_anagram("a", "aa"))              # False
print(is_anagram("abcd", "dcba"))         # True
print(is_anagram("python", "typhon"))     # True
print(is_anagram("listen", "silent"))     # True
print(is_anagram("apple", "papel"))       # True
print(is_anagram("hello", "bello"))       # False