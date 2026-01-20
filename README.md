# Task 4: Loops & Iterations 🌀

## 📌 Overview
This repository contains **Task 4: Loops & Iterations** completed as part of the **Python Developer Internship**.

The task focuses on understanding Python loops, iteration, control flow, and real-world use cases.

---

## 🛠 Tools Used
- Python  
- VS Code  

---

## 🔍 Concepts Covered
- for loop
- while loop
- break and continue
- Iterating over strings
- Multiplication tables
- range() with steps
- Loops with conditions
- Real-world loop examples

---

## 🧠 Complete Python Code (`loop_tasks.py`)

```python
# loop_tasks.py
# Task 4: Loops & Iterations
# Python Developer Internship

# 1. Print numbers from 1 to 100 using for loop
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# 2. Countdown timer using while loop
print("Countdown Timer:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Time's up!\n")

# 3. Demonstrating break and continue
print("Break and Continue Example:")
for i in range(1, 11):
    if i == 5:
        print("Breaking loop at", i)
        break
    if i == 3:
        continue
    print(i)
print()

# 4. Iterating over string characters
text = "Python"
print("Characters in string:")
for char in text:
    print(char)
print()

# 5. Multiplication table
num = 5
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# 6. Using range with steps
print("Even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# 7. Loop with conditions (Even/Odd check)
print("Even or Odd Check:")
numbers = [10, 15, 22, 33, 40]
for n in numbers:
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")
print()

# 8. Real-world example: Login attempts
print("Login Attempts Simulation:")
attempts = 3
while attempts > 0:
    print("Login attempts remaining:", attempts)
    attempts -= 1
print("Account locked due to multiple failed attempts.")
```
## Output
<img width="1367" height="719" alt="image" src="https://github.com/user-attachments/assets/94e095ee-19f4-4a2d-9578-66f53cae32e5" />
<img width="1154" height="776" alt="image" src="https://github.com/user-attachments/assets/4240c9ee-0691-43b2-8ba6-6a8eed9aa132" />

