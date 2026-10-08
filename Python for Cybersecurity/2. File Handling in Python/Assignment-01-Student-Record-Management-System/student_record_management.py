#Student Records Management (Only for developers)
# Before running the code, comment out the part of code (such as modes: r, w, a)

import os
from datetime import datetime

file_name = "student_records.txt"

print("====================================")
print("   Student Record Management System")
print("====================================")

# Check if file is already there
if os.path.exists(file_name):
    print("The student record file is already there.")
else:
    print("No record file found, so creating one...")

print("\nEnter details of the student")
print("----------------------------")

student_name = input("Student Name: ")
roll_number = input("Roll Number: ")
course_name = input("Course Name: ")

# Current date and time
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # Store first student record
with open(file_name, "w") as file:
    file.write("Student Name: " + student_name + "\n")
    file.write("Roll Number: " + roll_number + "\n")
    file.write("Course Name: " + course_name + "\n")
    file.write("Date & Time Added: " + date_time + "\n")
    file.write("--------------------------------\n")

print("\nDone! First student record has been saved.")

# Read and show the record
print("\nHere is the stored record:")
print("-------------------------")

with open(file_name, "r") as file:
    records = file.read()
    print(records)

# Add another student
print("\nAdd Another Student")
print("-------------------")

new_name = input("Student Name: ")
new_roll = input("Roll Number: ")
new_course = input("Course Name: ")

new_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add new record using append mode
with open(file_name, "a") as file:
    file.write("Student Name: " + new_name + "\n")
    file.write("Roll Number: " + new_roll + "\n")
    file.write("Course Name: " + new_course + "\n")
    file.write("Date & Time Added: " + new_date_time + "\n")
    file.write("--------------------------------\n")

print("\nNew student record added successfully!")

# Show all records
print("\nAll Student Records")
print("-------------------")

with open(file_name, "r") as file:
    print(file.read())

# Get file size
file_size = os.path.getsize(file_name)

print("File Information")
print("----------------")
print("File Name:", file_name)
print("File Size:", file_size, "bytes")

print("\nProgram completed. Thank you!")