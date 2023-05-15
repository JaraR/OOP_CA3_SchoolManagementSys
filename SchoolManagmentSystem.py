import json


class Student(object):
    """student class that is then inherited by English, History, and Math student class"""

    student_id_inc = 1

    def __init__(self, first_name, last_name):
        """initializes a student with an ID, first name, and last name"""
        self.student_id = str(Student.student_id_inc)
        self.first_name = first_name
        self.last_name = last_name
        Student.student_id_inc += 1

    def __str__(self):
        """returns a student's ID, first name, and last name"""
        return "ID: " + str(self.student_id) + " Name: " + self.first_name + " " + self.last_name

    def set_id(self, student_id):
        """will allow the Student ID to be set; mainly used for when loading from files"""
        self.student_id = student_id


class EnglishStudent(Student):
    """English student class that inherits from student class"""

    def __init__(self, first_name, last_name):
        """initializes an English student with an ID, first name, last name, course work, and an English grade"""
        Student.__init__(self, first_name, last_name)
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
        """allows coursework grades to be updated and changed through a menu"""
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

    def delete_data(self):
        """removes all data related to a student without deleting the student object itself"""
        self.attendance = 0
        self.final_exam = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.english_grade = 0


class HistoryStudent(Student):
    """History student class that inherits from student class"""

    def __init__(self, first_name, last_name):
        """initializes a History student with an ID, first name, last name, course work, and a History grade"""
        Student.__init__(self, first_name, last_name)
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
        """allows coursework grades to be updated and changed through a menu"""
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

    def delete_data(self):
        """removes all data related to a student without deleting the student object itself"""
        self.attendance = 0
        self.project = 0
        self.exam1 = 0
        self.exam2 = 0
        self.history_grade = 0


class MathStudent(Student):
    """Math student class that inherits from student class"""

    def __init__(self, first_name, last_name):
        """initializes a Math student with an ID, first name, last name, course work, and a Math grade"""
        Student.__init__(self, first_name, last_name)
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
        """allows coursework grades to be updated and changed through a menu"""
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

    def delete_data(self):
        """removes all data related to a student without deleting the student object itself"""
        self.quizzes = [0, 0, 0, 0, 0]
        self.quiz_avg = 0
        self.test1 = 0
        self.test2 = 0
        self.final_exam = 0
        self.math_grade = 0


class School(object):
    """school class that contains an aggregation of students"""

    def __init__(self):
        """initializes an empty school that contains a list of students"""
        self.students = []
        self.english_students = []
        self.history_students = []
        self.math_students = []

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

        if student.subject == "English":
            self.english_students.append(student)
        elif student.subject == "History":
            self.history_students.append(student)
        elif student.subject == "Math":
            self.math_students.append(student)

    def remove_student(self, student):
        """removes a student from the school's list of students"""
        self.students.remove(student)

        if student.subject == "English":
            self.english_students.remove(student)
        elif student.subject == "History":
            self.history_students.remove(student)
        elif student.subject == "Math":
            self.math_students.remove(student)

    def find_student_by_id(self, student_id):
        """finds and returns a student by their ID number"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    @staticmethod
    def calculate_grade(student):
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
        name = student.first_name + " " + student.last_name
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

    def save_file(self, filename):
        """saves student data to a json file for persistent memory"""
        data = []
        for student in self.students:
            student_data = {
                "student_id": student.student_id,
                "first_name": student.first_name,
                "last_name": student.last_name
            }
            if isinstance(student, EnglishStudent):
                student_data.update({
                    "attendance": student.attendance,
                    "final_exam": student.final_exam,
                    "quiz1": student.quiz1,
                    "quiz2": student.quiz2,
                    "subject": student.subject
                })
            elif isinstance(student, HistoryStudent):
                student_data.update({
                    "attendance": student.attendance,
                    "project": student.project,
                    "exam1": student.exam1,
                    "exam2": student.exam2,
                    "subject": student.subject
                })
            elif isinstance(student, MathStudent):
                student_data.update({
                    "quizzes": student.quizzes,
                    "test1": student.test1,
                    "test2": student.test2,
                    "final_exam": student.final_exam,
                    "subject": student.subject
                })
            data.append(student_data)

        with open(filename, "w") as file:
            json.dump(data, file)

    def save_subclass_file(self, student=None, sub_list=None):
        """saves student subclass data to a json file for persistent memory"""
        data = []
        if sub_list is not None:
            for student in sub_list:
                self.save_subclass_file(student)
        student_data = {
            "student_id": student.student_id,
            "first_name": student.first_name,
            "last_name": student.last_name
        }
        if isinstance(student, EnglishStudent):
            filename = "englishstudent.json"
            student_data.update({
                "attendance": student.attendance,
                "final_exam": student.final_exam,
                "quiz1": student.quiz1,
                "quiz2": student.quiz2,
                "subject": student.subject
            })
        elif isinstance(student, HistoryStudent):
            filename = "historystudent.json"
            student_data.update({
                "attendance": student.attendance,
                "project": student.project,
                "exam1": student.exam1,
                "exam2": student.exam2,
                "subject": student.subject
            })
        elif isinstance(student, MathStudent):
            filename = "mathstudent.json"
            student_data.update({
                "quizzes": student.quizzes,
                "test1": student.test1,
                "test2": student.test2,
                "final_exam": student.final_exam,
                "subject": student.subject
            })
        else:
            return
        data.append(student_data)

        with open(filename, "w") as file:
            json.dump(data, file)

    def load_file(self, filename):
        """reads student data from a json to continue data manipulation in a later session"""
        with open(filename, "r") as file:
            data = json.load(file)

        for student_data in data:
            student_id = student_data["student_id"]
            first_name = student_data["first_name"]
            last_name = student_data["last_name"]
            student = None

            if student_data["subject"] == "English":
                student = EnglishStudent(first_name, last_name)
                student.attendance = student_data["attendance"]
                student.final_exam = student_data["final_exam"]
                student.quiz1 = student_data["quiz1"]
                student.quiz2 = student_data["quiz2"]
            elif student_data["subject"] == "History":
                student = HistoryStudent(first_name, last_name)
                student.attendance = student_data["attendance"]
                student.project = student_data["project"]
                student.exam1 = student_data["exam1"]
                student.exam2 = student_data["exam2"]
            elif student_data["subject"] == "Math":
                student = MathStudent(first_name, last_name)
                student.quizzes = student_data["quizzes"]
                student.test1 = student_data["test1"]
                student.test2 = student_data["test2"]
                student.final_exam = student_data["final_exam"]
            # student.set_id(student_id)

            if student:
                # student.set_id(student_id)
                self.add_student(student)


def login():
    """allows users to log in to the system"""
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "pass":
        print("You're now logged in!")
        return True
    else:
        print("Incorrect username or password.")
        return False


def main():
    """an interactive command line menu that allows a user to login and perform CRUD operations on student data"""
    TUD = School()
    TUD.load_file("school.json")
    TUD.load_file("englishstudent.json")
    TUD.load_file("historystudent.json")
    TUD.load_file("mathstudent.json")
    logged_in = False

    while True:
        print("1: Login\n2: Add Student\n3: Remove Student\n4: Create/Update Student Data\n5: Read Student Data\n6: "
              "Delete Student Data\n7: Quit")
        user_input = input("Please select your choice, login is required before doing most operations: ")

        if user_input == "7":
            TUD.save_file("school.json")
            TUD.save_subclass_file(sub_list=TUD.english_students)
            TUD.save_subclass_file(sub_list=TUD.history_students)
            TUD.save_subclass_file(sub_list=TUD.math_students)
            print("Thank you for using TUD Student Management, goodbye!")
            return

        elif user_input == "1":
            print("Login")
            logged_in = login()

        elif user_input == "2" and logged_in:
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
                break
            TUD.add_student(student)
            TUD.save_subclass_file(student)
            TUD.save_file("school.json")
            print("Student has been added to TUD.")
            # print(TUD)

        elif user_input == "3" and logged_in:
            print("Remove Student")
            s_id = input("Enter the student's ID that you want to remove from the system: ")
            student = TUD.find_student_by_id(s_id)
            if isinstance(student, Student):
                print(student)
                confirmation = input("Are you sure you want to remove this student from the system? (y/n): ")
                if confirmation.lower() == "y":
                    TUD.remove_student(student)
                    TUD.save_subclass_file(student)
                    TUD.save_file("school.json")
                    print("Student has been removed from TUD.")
                elif confirmation.lower() == "n":
                    print("Removal has been canceled, returning to main menu.")
                    continue
                else:
                    print("Invalid input, returning to main menu.")
                    continue
            else:
                print("Student cannot be found.")

        elif user_input == "4" and logged_in:
            print("Create/Update Student Data")
            s_id = input("Enter the student's ID: ")
            student = TUD.find_student_by_id(s_id)
            if student:
                student.update_grades()
                TUD.save_file("school.json")
                TUD.save_subclass_file(student)
                print("Grades have been updated.")
            else:
                print("Student cannot be found.")

        elif user_input == "5" and logged_in:
            print("Read Student Data")
            s_id = input("Enter the student's ID: ")
            student = TUD.find_student_by_id(s_id)
            if student:
                TUD.student_report(student)
            else:
                print("Student cannot be found.")

        elif user_input == "6" and logged_in:
            print("Delete Student Data")
            s_id = input("Enter the student's ID: ")
            student = TUD.find_student_by_id(s_id)
            if student:
                student.delete_data()
                TUD.save_file("school.json")
                TUD.save_subclass_file(student)
                print("Student's grades have beem deleted.")
            else:
                print("Student cannot be found.")

        else:
            print("Please enter a valid input, or log in.")


# Main Program
main()  # Username: admin   Password: pass
