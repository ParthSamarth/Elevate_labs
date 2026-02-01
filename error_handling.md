# 🐍 Task 9 – Exception Handling & Logging in Python

## 📌 Project Overview

This project is part of the **Python Developer Internship – Task 9**, which focuses on implementing **exception handling and logging** in Python to build production-ready applications.

The goal of this task is to understand how to:
- Prevent program crashes  
- Handle runtime errors gracefully  
- Record errors into log files  
- Debug applications using logs  

This project uses Python’s built-in **logging module** and structured **try–except–else–finally** blocks.

---

## 🛠 Tools & Technologies

| Tool | Purpose |
|------|--------|
| Python 3.x | Core programming language |
| logging module | Error tracking and debugging |
| VS Code / Terminal | Development & execution |

---

## 🎯 Objectives

- Use try-except blocks to catch runtime errors  
- Handle multiple exception types  
- Implement custom exceptions  
- Use else and finally blocks  
- Log all errors to a file  
- Simulate common runtime issues  
- Debug using log records  

---
```
python
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class NegativeNumberError(Exception):
    pass

def divide_numbers(a, b):
    if a < 0 or b < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return a / b

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = divide_numbers(x, y)

except ZeroDivisionError as e:
    logging.error("Tried to divide by zero", exc_info=True)
    print("❌ Error: Cannot divide by zero.")

except ValueError as e:
    logging.error("Invalid input type", exc_info=True)
    print("❌ Error: Please enter valid integers.")

except NegativeNumberError as e:
    logging.error(str(e), exc_info=True)
    print(f"❌ Error: {e}")

except Exception as e:
    logging.error("Unexpected error", exc_info=True)
    print("❌ Something went wrong!")

else:
    print("✅ Result:", result)

finally:
    print("📁 Program finished. Check app.log for details.")
```
## Output
<img width="819" height="237" alt="image" src="https://github.com/user-attachments/assets/509a6e2b-a1fc-488e-982a-f7b52455d1ab" />



