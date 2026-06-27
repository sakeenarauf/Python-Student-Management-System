# STUDENT MANAGEMENT SYSTEM 

# Function to load students from file at start
def load_data():
    students = {}
    # Open file in read mode; if it doesn't exist, it creates an empty dict
    file = open("students.txt", "a+")
    file.seek(0)
    for line in file:
        # Each line is evaluated back into its dictionary structure
        if line:
            student = eval(line)
            students[student["id"]] = student
    file.close()
    return students

# Function to save all student data back to the file
def save_data(students):
    file = open("students.txt", "w")
    for s_id in students:
        file.write(str(students[s_id]) + "\n")
    file.close()

# 1. Add a new student record
def add_student(students):
    s_id = input("Enter Student ID: ")
    if s_id in students:
        print("Student ID already exists!")
        return
    
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    
    # Getting marks for 3 subjects
    m1 = float(input("Enter Marks for Subject 1: "))
    m2 = float(input("Enter Marks for Subject 2: "))
    m3 = float(input("Enter Marks for Subject 3: "))
    
    # Store everything in a nested dictionary
    students[s_id] = {
        "id": s_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": [m1, m2, m3]
    }
    save_data(students)
    print("Student added successfully!")

# 2. View all student records
def view_students(students):
    if not students:
        print("No student records found.")
        return
    for s_id in students:
        s = students[s_id]
        print("ID:", s["id"], "| Name:", s["name"], "| Age:", s["age"], "| Course:", s["course"], "| Marks:", s["marks"])

# 3. Search for a specific student
def search_student(students):
    s_id = input("Enter Student ID to search: ")
    if s_id in students:
        s = students[s_id]
        print("Record Found -> ID:", s["id"], "| Name:", s["name"], "| Marks:", s["marks"])
    else:
        print("Student not found.")

# 4. Update an existing student's details
def update_student(students):
    s_id = input("Enter Student ID to update: ")
    if s_id in students:
        print("Enter new details:")
        students[s_id]["name"] = input("New Name: ")
        students[s_id]["age"] = input("New Age: ")
        students[s_id]["course"] = input("New Course: ")
        save_data(students)
        print("Record updated successfully!")
    else:
        print("Student not found.")

# 5. Delete a student record
def delete_student(students):
    s_id = input("Enter Student ID to delete: ")
    if s_id in students:
        del students[s_id]
        save_data(students)
        print("Record deleted successfully!")
    else:
        print("Student not found.")

# 6. Calculate and display class statistics
def show_statistics(students):
    if not students:
        print("No data available to calculate statistics.")
        return
    
    total_class_marks = 0
    total_subjects_count = 0
    highest_mark = -1
    lowest_mark = 101
    top_student = ""
    top_avg = -1

    for s_id in students:
        s = students[s_id]
        student_total = s["marks"][0] + s["marks"][1] + s["marks"][2]
        student_avg = student_total / 3
        
        total_class_marks += student_total
        total_subjects_count += 3
        
        # Check for highest and lowest individual marks
        for m in s["marks"]:
            if m > highest_mark:
                highest_mark = m
            if m < lowest_mark:
                lowest_mark = m
                
        # Track the top performing student by highest average
        if student_avg > top_avg:
            top_avg = student_avg
            top_student = s["name"]

    print("--- Class Statistics ---")
    print("Class Average Mark:", total_class_marks / total_subjects_count)
    print("Highest Individual Mark:", highest_mark)
    print("Lowest Individual Mark:", lowest_mark)
    print("Top Performing Student:", top_student, "with Average:", top_avg)

# Main Menu-Driven Loop
def main():
    students = load_data()
    
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. View Class Statistics")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_statistics(students)
        elif choice == "7":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 7.")

# Run the application
main()