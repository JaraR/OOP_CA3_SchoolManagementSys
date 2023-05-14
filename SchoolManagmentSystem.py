class Student(object):
    """student class that is then inherited by English, History, and Math student class"""

    student_id = 1

    def __init__(self, first, last):
        """initializes a student with an ID, first name, and last name"""
        self.student_id = str(Student.student_id)
        self.first = first
        self.last = last
        Student.student_id += 1

    def __str__(self):
        """returns a student's ID, first name, and last name"""
        return "ID: " + str(self.student_id) + " Name: " + self.first + " " + self.last


class EnglishStudent(Student):
    """English student class that inherits from student class"""

    def __init__(self, first, last):
        """initializes an English student with an ID, first name, last name, course work, and an English grade"""
        Student.__init__(self, first, last)
        self.attendance = 0
        self.final_exam = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.english_grade = 0
        self.subject = "English"

    def __str__(self):
        """returns a student's ID, first name, last name, and English grade"""
        result_str = Student.__str__(self)
        result_str = result_str + " English grade: " + str(self.english_grade)
        return result_str

    def update_grades(self):
        print("Updating English student grades.")
        while True:
            print("1: Attendance\n2: Final Exam\n3: Quiz 1\n4: Quiz 2\n5: Quit\n")
            user_input = input("Please select your choice: ")
            if user_input == "1":
                print("Current Attendance grade: {}".format(self.attendance))
                try:
                    self.attendance = float(input("Enter Attendance grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "2":
                print("Current Final Exam grade: {}".format(self.final_exam))
                try:
                    self.final_exam = float(input("Enter Final Exam grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "3":
                print("Current Quiz 1 grade: {}".format(self.quiz1))
                try:
                    self.quiz1 = float(input("Enter Quiz 1 grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "4":
                print("Current Quiz 2 grade: {}".format(self.quiz2))
                try:
                    self.quiz2 = float(input("Enter Quiz 2 grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "5":
                print("Returning to main menu.")
                return
            else:
                print("Please enter a valid input.")


class HistoryStudent(Student):
    """History student class that inherits from student class"""

    def __init__(self, first, last):
        """initializes a History student with an ID, first name, last name, course work, and a History grade"""
        Student.__init__(self, first, last)
        self.attendance = 0
        self.project = 0
        self.exam1 = 0
        self.exam2 = 0
        self.history_grade = 0
        self.subject = "History"

    def __str__(self):
        """returns a student's ID, first name, last name, and History grade"""
        result_str = Student.__str__(self)
        result_str = result_str + " History grade: " + str(self.history_grade)
        return result_str

    def update_grades(self):
        print("Updating History student grades.")
        while True:
            print("1: Attendance\n2: Project\n3: Exam 1\n4: Exam 2\n5: Quit\n")
            user_input = input("Please select your choice: ")
            if user_input == "1":
                print("Current Attendance grade: {}".format(self.attendance))
                try:
                    self.attendance = float(input("Enter Attendance grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "2":
                print("Current Project grade: {}".format(self.project))
                try:
                    self.project = float(input("Enter Project grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "3":
                print("Current Exam 1 grade: {}".format(self.exam1))
                try:
                    self.exam1 = float(input("Enter Exam 1 grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "4":
                print("Current Exam 2 grade: {}".format(self.exam2))
                try:
                    self.exam2 = float(input("Enter Exam 2 grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "5":
                print("Returning to main menu.")
                return
            else:
                print("Please enter a valid input.")


class MathStudent(Student):
    """Math student class that inherits from student class"""

    def __init__(self, first, last):
        """initializes a Math student with an ID, first name, last name, course work, and a Math grade"""
        Student.__init__(self, first, last)
        self.quizzes = [0, 0, 0, 0, 0]
        self.quiz_avg = 0
        self.test1 = 0
        self.test2 = 0
        self.final_exam = 0
        self.math_grade = 0
        self.subject = "Math"

    def __str__(self):
        """returns a student's ID, first name, last name, and Math grade"""
        result_str = Student.__str__(self)
        result_str = result_str + " Math grade: " + str(self.math_grade)
        return result_str

    def update_grades(self):
        print("Updating Math student grades.")
        while True:
            print("1: Quizzes\n2: Test 1\n3: Test 2\n4: Final Exam\n5: Quit\n")
            user_input = input("Please select your choice: ")
            if user_input == "1":
                print("Current quiz grades: ", end="")
                for grade in self.quizzes:
                    print(grade, end=" ")
                print()
                try:
                    for index, value in enumerate(self.quizzes):
                        self.quizzes[index] = float(input("Enter quiz grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "2":
                print("Current Test 1 grade: {}".format(self.test1))
                try:
                    self.test1 = float(input("Enter Test 1 grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "3":
                print("Current Test 2 grade: {}".format(self.test2))
                try:
                    self.test2 = float(input("Enter Test 2 grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "4":
                print("Current Final Exam grade: {}".format(self.final_exam))
                try:
                    self.final_exam = float(input("Enter Final Exam grade: "))
                except ValueError:
                    print("You did not enter a number!")
            elif user_input == "5":
                print("Returning to main menu.")
                return
            else:
                print("Please enter a valid input.")


class School(object):
    """school class that contains an aggregation of students"""

    def __init__(self):
        """initializes an empty school that contains a list of students"""
        self.students = []

    def __str__(self):
        """returns a list of all the students"""
        all_students = ""
        for student in self.students:
            all_students += str(student) + " "
        return all_students
        # return str(self.students)

    def add_student(self, student):
        """adds a student to the school's list of students"""
        self.students.append(student)

    def remove_student(self, student):
        """removes a student from the school's list of students"""
        self.students.remove(student)

    def find_student_by_id(self, student_id):
        """finds and returns a student by their ID number"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def calculate_grade(self, student):
        """calculates a students weighted grade for each assignment type, including those with multiple assignments,
        and calculates the total grade"""
        if isinstance(student, EnglishStudent):
            grade = (student.attendance * 0.1) + (student.final_exam * 0.6) + (student.quiz1 * 0.15) + (
                    student.quiz2 * 0.15)
        elif isinstance(student, HistoryStudent):
            grade = (student.attendance * 0.1) + (student.project * 0.3) + (student.exam1 * 0.3) + (student.exam2 * 0.3)
        elif isinstance(student, MathStudent):
            quiz_avg = sum(student.quizzes) / 5
            student.quiz_avg = quiz_avg
            grade = (quiz_avg * 0.15) + (student.test1 * 0.15) + (student.test2 * 0.15) + (student.final_exam * 0.55)
        else:
            grade = 0
        return grade

    def student_report(self, student):
        """prints a well formatted student report"""
        grade = self.calculate_grade(student)
        name = student.first + " " + student.last
        print("ID: {:<5} {} Student: {:<26} Grade: {}".format(student.student_id, student.subject, name, grade))
        if isinstance(student, EnglishStudent):
            print("Attendance: {:>15}".format(student.attendance))
            print("Final Exam: {:>15}".format(student.final_exam))
            print("Quiz 1: {:>19}".format(student.quiz1))
            print("Quiz 2: {:>19}".format(student.quiz2))
        elif isinstance(student, HistoryStudent):
            print("Attendance: {:>15}".format(student.attendance))
            print("Project: {:>18}".format(student.project))
            print("Exam 1: {:>19}".format(student.exam1))
            print("Exam 2: {:>19}".format(student.exam2))
        elif isinstance(student, MathStudent):
            print("Quizzes: {:>18}".format(student.quiz_avg))
            print("Test 1: {:>19}".format(student.test1))
            print("Test 2: {:>19}".format(student.test2))
            print("Final Exam: {:>15}".format(student.final_exam))



def main():
    """an interactive command line menu that allows a user to login and perform CRUD operations on student data"""
    TUD = School()

    while True:
        print("1: Login\n2: Add Student \n3: Remove Student\n4: Create Student Data\n5: Read Student Data\n6: Update "
              "Student Data\n7: Delete Student Data\n8: Quit")
        user_input = input("Please select your choice, login is required before doing most operations: ")

        if user_input == "8":
            print("Thank you for using TUD Student Management, goodbye!")
            return
        elif user_input == "1":
            print("Login")
        elif user_input == "2":
            print("Add Student")
            f_name = input("Enter the student's first name: ")
            l_name = input("Enter the student's last name: ")
            course = input("Enter the course that the student will be taking (English, History, or Math): ")

            if course.lower() == "english":
                student = EnglishStudent(f_name, l_name)
            elif course.lower() == "history":
                student = HistoryStudent(f_name, l_name)
            elif course.lower() == "math":
                student = MathStudent(f_name, l_name)
            else:
                print("Please make sure that the course is correct.")
                continue

            TUD.add_student(student)
            # save addition
            print("Student has been added to TUD.")
            print(TUD)

        elif user_input == "3":
            print("Remove Student")
            s_id = input("Enter the student's ID that you want to remove from the system: ")
            student = TUD.find_student_by_id(s_id)
            if isinstance(student, Student):
                print(student)
                confirmation = input("Are you sure you want to remove this student from the system? (y/n): ")
                if confirmation.lower() == "y":
                    TUD.remove_student(student)
                    print("Student has been removed from TUD.")
                    # save deletion
                elif confirmation.lower() == "n":
                    print("Removal has been canceled, returning to main menu.")
                    continue
                else:
                    print("Invalid input, returning to main menu.")
                    continue
            else:
                print("Student cannot be found.")

        elif user_input == "4":
            print("Create Student Data")
        elif user_input == "5":
            print("Read Student Data")
            s_id = input("Enter the student's ID: ")
            student = TUD.find_student_by_id(s_id)
            if student:
                TUD.student_report(student)
            else:
                print("Student cannot be found.")
        elif user_input == "6":
            print("Update Student Data")
        elif user_input == "7":
            print("Delete Student Data")
        else:
            print("Please enter a valid input.")


# Main Program
# main()
student1 = EnglishStudent("John", "Doe")
print(student1)

student2 = HistoryStudent("Jane", "Doe")
print(student2)

student3 = MathStudent("Dane", "Joe")
print(student3)

student4 = MathStudent("Elizabeth", "McConnell")
print(student4)

TUD = School()
TUD.add_student(student1)
TUD.add_student(student2)
TUD.add_student(student3)
TUD.add_student(student4)
print(TUD)

print(TUD.find_student_by_id(2))

TUD.remove_student(student2)
print(TUD)

for x in TUD.students:
    print(x)

TUD.student_report(student4)

student1.update_grades()
student2.update_grades()
student3.update_grades()

TUD.student_report(student1)
TUD.student_report(student2)
TUD.student_report(student3)
