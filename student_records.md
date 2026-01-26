# 📌 Task 7 – Dictionaries & JSON Handling (Python Developer Internship)

This project is part of the **Python Developer Internship** program.  
The objective of this task is to understand how **structured data** is stored, accessed, updated, and exchanged using **Python dictionaries and JSON files**.

This task simulates a real-world system where student records are stored, modified, saved, and retrieved.

---

## 🧠 Concepts Covered

This task demonstrates the following important Python concepts:

- Dictionaries and key–value pairs  
- Accessing dictionary keys and values  
- Updating and deleting dictionary data  
- Looping through nested dictionaries  
- Converting Python dictionaries into JSON  
- Saving JSON data into a file  
- Reading JSON data back into Python  
- Displaying formatted output  

These concepts are commonly used in:
- Backend development  
- APIs  
- Databases  
- Data storage systems  
- Web applications  

---

## 📂 Project Structure

## Code
```
python
import json

# 1. Store student details using dictionary
students = {
    101: {"name": "Parth", "age": 21, "course": "B.Tech", "marks": 85},
    102: {"name": "Riya", "age": 20, "course": "BCA", "marks": 90},
    103: {"name": "Aman", "age": 22, "course": "B.Sc", "marks": 78}
}

print("\n--- Original Student Records ---")
for roll, data in students.items():
    print(roll, ":", data)

# 2. Access keys and values
print("\nAccessing Keys:", students.keys())
print("Accessing Values:", students.values())

# 3. Update an entry
students[101]["marks"] = 88

# 4. Delete an entry
del students[103]

# 5. Loop through dictionary
print("\n--- Updated Student Records ---")
for roll, info in students.items():
    print(f"Roll No: {roll}")
    for key, value in info.items():
        print(f"   {key}: {value}")

# 6. Convert dictionary to JSON
json_data = json.dumps(students, indent=4)

# 7. Save JSON to file
with open("students.json", "w") as file:
    file.write(json_data)

print("\nData saved to students.json")

# 8. Read JSON back into Python
with open("students.json", "r") as file:
    data_from_json = json.load(file)

# 9. Print clean formatted output
print("\n--- Data Read From JSON File ---")
for roll, info in data_from_json.items():
    print(f"Roll No: {roll}")
    for key, value in info.items():
        print(f"   {key}: {value}")
```
## Output
<img width="1613" height="651" alt="image" src="https://github.com/user-attachments/assets/e384fa8f-9d4c-4c8a-a71d-806ec303bb3d" />
<img width="1667" height="376" alt="image" src="https://github.com/user-attachments/assets/56640a88-2aeb-4431-aae1-3908cd42ea02" />

