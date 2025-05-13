# Problem: Merge Intervals (Medium)
# You are given an array of intervals, where intervals[i] = [start_i, end_i],
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Why? Intervals [1,3] and [2,6] overlap → merged to [1,6]


# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Why? Intervals touch at 4 → considered overlapping

# Constraints:
# 1 <= len(intervals) <= 10⁴
# intervals[i][0] <= intervals[i][1]
# Output should be sorted by start time

# | Metric | Value      | Why                                              |
# | ------ | ---------- | ------------------------------------------------ |
# | Time   | O(n log n) | Due to sorting step                              |
# | Space  | O(n)       | In worst case, no overlaps → all intervals added |


def merge_intervals(intervals): 
  intervals.sort(key=lambda x: x[0])

  merged = []

  for interval in intervals:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

  return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # → [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]]))                 # → [[1,5]]
print(merge_intervals([[1,2],[3,4],[2,3],[4,5]]))     # → [[1,5]]
print(merge_intervals([[1,10],[2,3],[4,5]]))          # → [[1,10]]