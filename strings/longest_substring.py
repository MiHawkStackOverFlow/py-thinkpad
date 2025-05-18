# Problem: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with length = 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with length = 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with length = 3.

# Time & Space Complexity:
# Time: O(n)
# Space: O(n)

def length_of_longest_substring(s):
  char_index = {}     # stores latest index of each character
  start = 0           # left side of the sliding window
  max_length = 0      # track the maximum length found

  for i, char in enumerate(s):
    # f is short for "formatted string literal", introduced in Python 3.6. It allows you to embed variables directly inside strings.
    print(f"\nChecking '{char}' at index {i}")
    print(f"Current window: '{s[start:i]}'")

    # Check if the character was seen before AND is inside the current window
    if char in char_index and char_index[char] >= start:
      print(f"Duplicate '{char}' found. Previous index = {char_index[char]}")
      # Move the start just after the last occurrence
      start = char_index[char] + 1
      print(f"Start moved to {start}")

    # Update the last seen index of the current character
    char_index[char] = i
    print(f"char_index updated: {char_index}")

    # Calculate the window length
    window_length = i - start + 1
    max_length = max(max_length, window_length)
    print(f"Updated max_length = {max_length}")

  return max_length

print(length_of_longest_substring("abcabcbb"))     # Expected: 3 ("abc")
print(length_of_longest_substring("bbbbb"))        # Expected: 1 ("b")
print(length_of_longest_substring("pwwkew"))       # Expected: 3 ("wke")
print(length_of_longest_substring("aab"))          # Expected: 2 ("ab")
print(length_of_longest_substring("dvdf"))         # Expected: 3 ("vdf")
