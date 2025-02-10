def read_file(): # WORKS!
    # open file
    file = open('M2/grades.txt', 'r')
    # read the file
    lines = file.readlines()
    # Put students in a list
    students = []
    for line in lines:
        stuName, stuID, courseName, courseGrade = line.strip().split(", ")
        students.append((stuName, stuID, courseName, courseGrade))
    # close the file
    file.close() 
    return students

def write_file(students):
    with open('M2/grades.txt', 'w') as file:
        for stuName, stuID, courseName, courseGrade in students:
            file.write(f"{stuName}, {stuID}, {courseName}, {courseGrade} \n")
        file.close()

# add a student record func() WORKS!
def add_record(students):
    stuName = input("Enter student name: ")
    stuID = input("Enter student ID: ")
    courseName = input("Enter course name: ")
    courseGrade = input("Enter course grade: ")
    # add student to the list
    students.append((stuName, stuID, courseName, courseGrade))
    print("Student has been added.\n")
    print_students(students)

# print all student records func() WORKS!
def print_students(students):
    print("All Students:")
    for stuName, stuID, courseName, courseGrade in students:
        print(f"Student Name: {stuName}, Student ID: {stuID}, Course Name: {courseName}, Course Grade: {courseGrade} \n")

# search for a student func()
def search_student(students, stuSearch):
    found = False
    with open('M2/grades.txt', 'r') as file: 
        lines = file.readlines()
        for stuName, stuID, courseName, courseGrade in students: 
            if stuID == stuSearch:
                print(f"Student has been found!\n")
                print(f"Student Name: {stuName}, ID: {stuID}, course name: {courseName}, course grade: {courseGrade}\n")
                found = True
                break
    if not found:
        print("No record for student found.\n")

# update student grade func()
def update_grade(students, stuSearch):
    newGrade = input("Enter a new grade for student: ")
    updated = False
    for index, (stuName, stuID, courseName, courseGrade) in  enumerate(students):
        if stuID == stuSearch:
            students[index] = (stuName, stuID, courseName, newGrade)
            updated = True
            break
    if updated:
        #write_file(students) used for testing
        print(f"Student with ID {stuSearch} grade has been updated to {newGrade} \n")
        print_students(students)

# delete a student record func()
def delete_student(students, stuSearch):
    deleted = False
    # Remove the record
    for i in range(len(students)):
        if students[i][1] == stuSearch:
           del students[i]
           deleted = True
           break

    if deleted:
        # write_file(students) used for testing
        print(f"Student with ID {stuSearch} deleted.\n")    
        print_students(students)

# main func()
def main():
    students = read_file()
    print("Enter 1 to add student record")
    print("Enter 2 to view all student records")
    print("Enter 3 to search for a student by ID")
    print("Enter 4 to update student grade")
    print("Enter 5 to delete a student record")
    print("Enter 0 to exit")
    choice = input("Enter your choice: ")
    print("\n")

    while choice != '0':
       if choice == '1':
           add_record(students)
       elif choice == '2':
           print_students(students)
       elif choice == '3':
           stuSearch = input("Enter the student ID: ")
           search_student(students, stuSearch)
       elif choice =='4':
           stuSearch = input("Enter the student ID: ")
           search_student(students, stuSearch)
           update_grade(students, stuSearch)
       elif choice == '5':
           stuSearch = input("Enter the ID of student to delete: ")
           search_student(students, stuSearch)
           delete_student(students, stuSearch)
       elif choice == '0':
           print("Exiting...")
           break
       else:
           print("This is not an option. Please try again.")
       print("Enter 1 to add student record")
       print("Enter 2 to view all student records")
       print("Enter 3 to search for a student by ID")
       print("Enter 4 to update student record")
       print("Enter 5 to delete a student record")
       print("Enter 0 to exit")
       choice = input("Enter your choice: ")

if __name__ == "__main__":
    main()
