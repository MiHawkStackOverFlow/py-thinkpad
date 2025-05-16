# py-thinkpad

This is my personal Python learning and problem-solving space. It includes:

- Python DSA practice (Arrays, HashMaps, Intervals, etc.)
- Concept notes as I explore more of Python
- Real-world problem breakdowns
- Clean code logic (for my own reference)


### ✅ Big-O Complexity Cheat Sheet (Time & Space)

---

### ⏱️ Time Complexity

| Big-O     | Name               | What It Means                             | Real-World Analogy                          |
|-----------|--------------------|-------------------------------------------|---------------------------------------------|
| O(1)      | Constant time      | Always takes same time, no matter input   | Getting the 5th element in a list           |
| O(log n)  | Logarithmic time   | Input shrinks fast (usually via divide)   | Binary search (cut in half each time)       |
| O(n)      | Linear time        | Time grows directly with input size       | Looping through a list                      |
| O(n log n)| Log-linear time    | Sorting + linear logic                    | Sorting then looping                        |
| O(n²)     | Quadratic time     | Nested loops on n items                   | Comparing all pairs in a list               |
| O(2ⁿ)     | Exponential time   | Doubles with each input step              | Recursive problems like Fibonacci           |

---

### 💾 Space Complexity

| Big-O     | Name                | What It Means                                 | Example                                       |
|-----------|-------------------- |-----------------------------------------------|-----------------------------------------------|
| O(1)      | Constant space      | No extra memory grows with input              | Two pointers or counters                      |
| O(n)      | Linear space        | Memory grows with input size                  | Copying array, using hash maps                |
| O(n²)     | Quadratic space     | Memory grows with every pair or matrix cell   | 2D matrix, dynamic programming table          |

---

### 🧠 Visualizing Time Complexity (n = 10,000)

| Big-O     | Approx Steps |
|-----------|--------------|
| O(1)      | 1            |
| O(log n)  | ~13          |
| O(n)      | 10,000       |
| O(n log n)| ~130,000     |
| O(n²)     | 100,000,000  |
| O(2ⁿ)     |  HUGE        |

---

### ✅ Example Code Mapping

| Code                                | Time Complexity  |
|-------------------------------------|------------------|
| `for i in nums:`                    | O(n)             |
| `nums.sort()`                       | O(n log n)       |
| `for i in nums: for j in nums:`     | O(n²)            |
| `dict[key]` lookup                  | O(1)             |
| `while low <= high:` (binary)       | O(log n)         |

---

### 🌍 Real-World Analogy Summary

| Scenario                               | Likely Complexity | Reason                                                 |
|----------------------------------------|-------------------|--------------------------------------------------------|
| Searching a contact alphabetically     | O(log n)          | Like binary search in a sorted list                    |
| Reading all emails in inbox            | O(n)              | You go through each one linearly                       |
| Checking if a name exists in contacts  | O(1)              | Using a hashmap or dictionary                          |
| Comparing every person to every other  | O(n²)             | Nested comparisons, like in brute-force similarity     |
| Sorting contacts then searching        | O(n log n)        | Sort takes n log n, search is log n                    |

