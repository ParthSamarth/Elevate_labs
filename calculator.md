# 🧮 Modular Calculator – Python Internship Task 5

This project is part of **Python Developer Internship – Task 5 (Functions & Modular Programming)**.  
The goal is to build a calculator using Python functions and modular programming principles.

---

## 📌 Objective
- Use functions for operations
- Apply default arguments
- Handle errors (division by zero)
- Follow DRY principle
- Build a menu-driven program

---

## 🛠 Features
- Addition
- Subtraction
- Multiplication
- Division
- Division by zero handling
- User input based menu

---

## ▶ How to Run

Open terminal in the project folder and run:

```bash
python calculator.py
```
``` python
def add(a, b=0):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b=0):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b=1):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b=1):
    """Returns the division of two numbers. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def calculator():
    """Main calculator function that takes user input"""

    print("----- Simple Modular Calculator -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1-4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    calculator()
```
## Output
<img width="757" height="321" alt="image" src="https://github.com/user-attachments/assets/4924d0b4-0a41-4ac6-942b-fc805007f66d" />
