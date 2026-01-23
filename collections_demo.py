# -------- LIST --------
students = ["Parth", "Amit", "Neha", "Riya", "Amit"]

print("Original List:", students)

# Add a student
students.append("Rahul")
print("After Adding Rahul:", students)

# Remove a student
students.remove("Neha")
print("After Removing Neha:", students)

# Sort list
students.sort()
print("Sorted List:", students)


# -------- TUPLE --------
# Tuple for fixed data (immutable)
college_info = ("ABC Engineering College", 2025)
print("\nCollege Info (Tuple):", college_info)


# -------- SET --------
# Convert list to set to remove duplicates
student_set = set(students)
print("\nSet (Duplicates Removed):", student_set)

# Another set
new_students = {"Riya", "Karan", "Amit"}

# Set operations
print("\nUnion:", student_set.union(new_students))
print("Intersection:", student_set.intersection(new_students))
print("Difference:", student_set.difference(new_students))


# -------- ITERATION --------
print("\nIterating over student set:")
for s in student_set:
    print(s)


# -------- MUTABLE vs IMMUTABLE --------
print("\nMutable vs Immutable")
print("List is mutable (can change)")
students.append("Sonal")
print("Updated List:", students)

print("Tuple is immutable (cannot change)")
# college_info[0] = "XYZ College"   # This will give an error


# -------- FORMATTED OUTPUT --------
print("\nFormatted Output:")
print(f"Total Students in List: {len(students)}")
print(f"Total Unique Students: {len(student_set)}")
