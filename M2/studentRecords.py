def read_file():
    # open file
    file = open('grades.txt', 'r')

    # read the file
    # content = file.read()

    # print(content)
    lines = file.readlines()

    for line in lines:
        print(line)

    # close the file
    file.close() 
    return
# add a student record func()
def add_record():
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
