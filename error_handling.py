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
