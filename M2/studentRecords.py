def read_file():
    # open file
    file = open('M2/grades.txt', 'r')

    # read the file
    lines = file.readlines()

    for line in lines:
        stuName, stuID, courseName, courseGrade = line.strip().split(", ")
        print(f"Name: {stuName}, ID: {stuID}, Course: {courseName}, Grade: {courseGrade} ")

    # close the file
    file.close() 
    
    return stuName, stuID, courseName, courseGrade

# add a student record func()
def add_record():
    # write to file
    return

# print all student records func()
def print_students():
    return

# search for a student func()
def search_student():
    return

# update student grade func()
def update_grade():
    return

# delete a student record func()
def delete_student():
    return

# main func()
def main():
    read_file()
    return

if __name__ == "__main__":
    main()
