### 1️⃣ Traversal (Arrays & Strings)
####🔹 What is Traversal?

Traversal means visiting each element/character one by one.

🔸 Array Traversal
Example
```python
arr = [10, 20, 30, 40]

for x in arr:
    print(x)
```
📌 Output:

```text
10
20
30
40
```

Index-based traversal
```python
for i in range(len(arr)):
    print(f"Index {i} → Value {arr[i]}")
```

🔸 String Traversal
```python
s = "HELLO"

for ch in s:
    print(ch)
```

📌 Strings are arrays of characters.

💡 Common Traversal Use Cases
- Find sum / max / min
- Count frequency
- Search an element
- Reverse a string/array

### 2️⃣ Two Pointers Technique
🔹 What is Two Pointers?

Use two indices (usually left & right) to process data efficiently.

🔸 Example 1: Reverse an Array
```python
arr = [1, 2, 3, 4, 5]

left, right = 0, len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
```


📌 Output:
```text
[5, 4, 3, 2, 1]
```
🔸 Example 2: Check Palindrome (String)
```python
s = "madam"

left, right = 0, len(s) - 1
is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)
```

📌 Output:
```text
True
```
💡 When to Use Two Pointers?

✔ Sorted arrays
✔ Reversal problems
✔ Palindrome checking
✔ Pair problems (sum = target)

### 3️⃣ Sliding Window Technique
🔹 What is Sliding Window?

A window (subarray/substring) that moves across data to avoid nested loops.

🔸 Fixed Size Sliding Window
Problem: Maximum sum of subarray of size k
```python
arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i]      # add next element
    window_sum -= arr[i - k]  # remove previous element
    max_sum = max(max_sum, window_sum)

print(max_sum)
```

📌 Output:

```text
9
```
🔸 Variable Size Sliding Window (Strings)
Problem: Longest substring without repeating characters
```python
s = "abcabcbb"
char_set = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)
```

📌 Output:
```text
3
```
💡 When to Use Sliding Window?

✔ Subarrays / substrings
✔ Maximum / minimum range
✔ Longest / shortest conditions
✔ Optimizing O(n²) → O(n)

#### 🔥 Quick Comparison

| Technique	| Best For	Time |
| ------- | --------------- |
| Traversal	| Simple processing | 	O(n)| 
| Two Pointers | 	Reversal, pairs| 	O(n) | 
| Sliding Window | 	Subarray problems | 	O(n) | 

#### 🎯 Interview Tip

If the problem says subarray / substring, think Sliding Window
If it says reverse / pair / palindrome, think Two Pointers