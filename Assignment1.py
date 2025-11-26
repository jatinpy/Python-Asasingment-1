# Name- Jatin Sehrawat
# Roll No- 2501660030
# Program- BCA Cyber
# Course- Python
# Code- ETCCCPP103

import os

print("\n----------------------------------------")
print("  STEP 1: COLLECTING STUDENT DETAILS")
print("----------------------------------------")

name = input("Enter Full Name: ")
roll_no = input("Enter Roll No: ")
course = input("Enter Course Name: ")
university = input("Enter University Name: ")
city = input("Enter City: ")
age_input = input("Enter Age: ")
hobby = input("Enter Main Hobby: ")

try:
    age = int(age_input)
except ValueError:
    age = 0
    print("[ERROR] Invalid age entered. Setting Age to 0 for calculations.")


print("\n----------------------------------------")
print("  STEP 2: DEMONSTRATING OPERATORS")
print("----------------------------------------")

current_year = 2025
next_year = current_year + 1
age_in_5_years = age + 5
print(f"Arithmetic: Age in 5 years will be {age_in_5_years}")

is_adult = age >= 18
print(f"Comparison: Is the student an adult (>= 18)? {is_adult}")

is_eligible = is_adult and (course.upper() == "BCA")
print(f"Logical: Is student eligible for Special Course? (Adult AND BCA)? {is_eligible}")

message = "Welcome to "
message += "Python Programming !"
print(f"Concatenation: {message}")


print("\n----------------------------------------")
print("  STEP 3: STRING OPERATIONS & METHODS")
print("----------------------------------------")

first_name = name.split()[0]
last_name = name.split()[-1]
print(f"Slicing: First character of Roll No is: '{roll_no[0]}'")

print(f"Escape Characters: Roll No:\t{roll_no}\nName:\t\t{name}")

print(f"F-String: Hello, {first_name}! Your course is {course}.")

print("\n--- String Methods ---")
print(f"1. .title(): Hobby (Title Case): {hobby.title()}")
print(f"2. .upper(): Roll No (Uppercase): {roll_no.upper()}")
print(f"3. .strip(): Name (Stripped): '{name.strip()}'")
print(f"4. .replace(): University Name (Hyphenated): {university.replace(' ', '-')}")
print(f"5. .count(): Count of 'a' in Name: {name.lower().count('a')}")
print(f"6. .isalpha(): Is Course all letters? {course.replace(' ', '').isalpha()}")


print("\n----------------------------------------")
print("        STUDENT PROFILE SYSTEM")
print("----------------------------------------")

print(f"Name:{'':<10}{name.title()}")
print(f"Roll No:{'':<7}{roll_no.upper()}")
print(f"Course:{'':<8}{course.upper()}")
print(f"University:{'':<4}{university.title()}")
print(f"City:{'':<10}{city.title()}")
print(f"Age:{'':<11}{age}")
print(f"Hobby:{'':<9}{hobby.title()}")
print("----------------------------------------")
print(f"{message}")


print("\n----------------------------------------")
print("        BONUS TASK: FILE SAVE")
print("----------------------------------------")

save_profile = input("Do you want to save your profile? (yes/no): ")

if save_profile.lower() == "yes":
    file_name = "student_profile.txt"
    file_content = f"""
STUDENT PROFILE DATA
========================================
Name: {name.title()}
Roll No: {roll_no.upper()}
Course: {course.upper()}
University: {university.title()}
City: {city.title()}
Age: {age}
Hobby: {hobby.title()}
========================================
Operators Demo:
Age in 5 years: {age_in_5_years}
Is Adult (>=18): {is_adult}
Eligible for Special Course: {is_eligible}
String Methods Used: 6
"""
    try:
        with open(file_name, 'w') as f:
            f.write(file_content)
        print(f"[SUCCESS] Profile successfully saved to '{file_name}'")
        print("A text log file has been created.")
    except IOError as e:
        print(f"[ERROR] Could not write to file: {e}")
else:
    print("Profile will not be saved. Thank you!")
