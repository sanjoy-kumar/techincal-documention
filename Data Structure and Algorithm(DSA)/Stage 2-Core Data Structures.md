### 1️⃣ What is an Array?

**Answer:** An array is a collection of elements stored at continuous memory locations and accessed using an index.

👉 Think of it as a row of boxes, where each box holds one value.

### 2️⃣ Why Do We Need Arrays?

Without arrays:
- You would need many variables (a1, a2, a3, a4…)

With arrays:
- You store multiple values in one variable
- Easy to access, update, loop, and process data

### 3️⃣ Basic Structure of an Array

Example (Numbers)
arr = [10, 20, 30, 40, 50]

Visual Representation (Image)

Index →   0     1     2     3     4
        ┌─────┬─────┬─────┬─────┬─────┐
Array → │ 10  │ 20  │ 30  │ 40  │ 50  │
        └─────┴─────┴─────┴─────┴─────┘


📌 Index always starts from 0

### 4️⃣ Accessing Elements in an Array

Syntax

```python
array[index]
```

Example

```python
arr = [10, 20, 30, 40]
print(arr[0])   # 10
print(arr[2])   # 30
```

Visual

arr[2]
   ↓
┌─────┬─────┬─────┬─────┐
│ 10  │ 20  │ 30  │ 40  │
└─────┴─────┴─────┴─────┘

### 5️⃣ Updating an Element

Example

```python
arr = [10, 20, 30]
arr[1] = 99
print(arr)
```

Output
```text
[10, 99, 30]
```

Visual

Before:  [10, 20, 30]
                 ↑
After:   [10, 99, 30]

### 6️⃣ Length of an Array

Example

```python
arr = [5, 15, 25, 35]
print(len(arr))
```

Output
4


📌 Length = number of elements

### 7️⃣ Traversing an Array (Looping)

Example using for
```python
arr = [10, 20, 30]
for x in arr:
    print(x)
```

Visual Flow

10 → 20 → 30

### 8️⃣ Inserting Elements
Add at the end
```python
arr = [1, 2, 3]
arr.append(4)
```

Visual

Before: [1, 2, 3]
After:  [1, 2, 3, 4]

Insert at a specific index
```python
arr.insert(1, 99)
```

Index:   0   1   2   3
Before: [1,  2,  3,  4]
After:  [1, 99,  2,  3,  4]

### 9️⃣ Deleting Elements
Remove by value
```python
arr.remove(99)
```

Remove by index
arr.pop(2)

Visual
Before: [1, 99, 2, 3]
Remove index 2 → value 2
After:  [1, 99, 3]

🔟 Types of Arrays (Conceptually)
1️⃣ One-Dimensional Array
[10, 20, 30, 40]

2️⃣ Two-Dimensional Array (Matrix)
matrix = [
    [1, 2],
    [3, 4]
]

Visual (2D Image)
┌───┬───┐
│ 1 │ 2 │
├───┼───┤
│ 3 │ 4 │
└───┴───┘

1️⃣1️⃣ Real-World Example
Marks of Students
marks = [78, 85, 90, 66]

Student 1 → 78
Student 2 → 85
Student 3 → 90
Student 4 → 66

1️⃣2️⃣ Time Complexity (Basic Idea)
Operation	Time
Access	O(1)
Search	O(n)
Insert	O(n)
Delete	O(n)