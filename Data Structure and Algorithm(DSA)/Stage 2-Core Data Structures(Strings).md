1️⃣ What is a String?

A string is a sequence of characters (letters, numbers, symbols, spaces).

👉 Each character is stored in order and can be accessed using an index, just like an array.

Example
s = "HELLO"

2️⃣ String as a Character Array

Internally, a string behaves like an array of characters.

Visual Representation (Image)
Index →   0     1     2     3     4
        ┌─────┬─────┬─────┬─────┬─────┐
String→ │  H  │  E  │  L  │  L  │  O  │
        └─────┴─────┴─────┴─────┴─────┘


📌 Index always starts from 0

3️⃣ Creating Strings
Using quotes
s1 = "Hello"
s2 = 'World'

Multiline string
s3 = """Hello
World"""

4️⃣ Accessing Characters
Syntax
string[index]

Example
s = "PYTHON"
print(s[0])   # P
print(s[3])   # H

Visual
s[3]
  ↓
┌─────┬─────┬─────┬─────┬─────┬─────┐
│  P  │  Y  │  T  │  H  │  O  │  N  │
└─────┴─────┴─────┴─────┴─────┴─────┘

5️⃣ Negative Indexing

Python allows indexing from the end.

Example
s = "HELLO"
print(s[-1])   # O
print(s[-3])   # L

Visual
Index →  -5   -4   -3   -2   -1
         H    E    L    L    O

6️⃣ String Length
Example
s = "DSA"
print(len(s))

Output
3


📌 Length = number of characters (including spaces)

7️⃣ Traversing a String
Using loop
s = "CODE"
for ch in s:
    print(ch)

Flow (Image)
C → O → D → E

8️⃣ String Immutability (Very Important)

🔴 Strings are immutable
You cannot change characters directly.

❌ Invalid
s = "HELLO"
s[0] = "Y"   # Error

✅ Correct way
s = "HELLO"
s = "Y" + s[1:]
print(s)

Visual
Old:  HELLO
New:  YELLO

9️⃣ String Slicing
Syntax
string[start : end]


📌 end index is excluded

Example
s = "PYTHON"
print(s[1:4])

Output
YTH

Visual
Index →   0   1   2   3   4   5
          P   Y   T   H   O   N
              └───────┘

🔟 Common String Operations
Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

Hello World

Repetition
print("Hi" * 3)

HiHiHi

Membership
print("A" in "DATA")   # True

1️⃣1️⃣ Common String Methods
Method	Example	Result
upper()	"hi".upper()	HI
lower()	"HI".lower()	hi
strip()	" hi ".strip()	hi
replace()	"abc".replace("a","x")	xbc
split()	"a,b,c".split(",")	['a','b','c']
1️⃣2️⃣ Real-World Example
Email Validation (Simple)
email = "user@gmail.com"
if "@" in email:
    print("Valid format")

1️⃣3️⃣ Time Complexity (Basic)
Operation	Time
Access	O(1)
Traversal	O(n)
Concatenation	O(n)
Search	O(n)