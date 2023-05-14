class Student(object):
    """student class that is then inherited by English, History, and Math student class"""

    student_id = 1

    def __init__(self, first, last):
        """initializes a student with an ID, first name, and last name"""
        self.student_id = Student.student_id
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
        self.english_grade = (self.attendance * 0.1) + (self.final_exam * 0.6) + (self.quiz1 * 0.15) + (
                self.quiz2 * 0.15)

    def __str__(self):
        """returns a student's ID, first name, last name, and English grade"""
        result_str = Student.__str__(self)
        result_str = result_str + " English grade: " + str(self.english_grade)
        return result_str


class HistoryStudent(Student):
    """History student class that inherits from student class"""

    def __init__(self, first, last):
        """initializes a History student with an ID, first name, last name, course work, and a History grade"""
        Student.__init__(self, first, last)
        self.attendance = 0
        self.project = 0
        self.exam1 = 0
        self.exam2 = 0
        self.history_grade = (self.attendance * 0.1) + (self.project * 0.3) + (self.exam1 * 0.3) + (self.exam2 * 0.3)

    def __str__(self):
        """returns a student's ID, first name, last name, and History grade"""
        result_str = Student.__str__(self)
        result_str = result_str + " History grade: " + str(self.history_grade)
        return result_str


class MathStudent(Student):
    """Math student class that inherits from student class"""

    def __init__(self, first, last):
        """initializes a Math student with an ID, first name, last name, course work, and a Math grade"""
        Student.__init__(self, first, last)
        self.quizzes = [0, 0, 0, 0, 0]
        self.test1 = 0
        self.test2 = 0
        self.final_exam = 0
        self.math_grade = (self.quizzes * 0.15) + (self.test1 * 0.15) + (self.test2 * 0.15) + (self.final_exam * 0.55)

    def __str__(self):
        """returns a student's ID, first name, last name, and Math grade"""
        result_str = Student.__str__(self)
        result_str = result_str + " Math grade: " + str(self.math_grade)
        return result_str


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


# Main Program
student1 = Student("John", "Doe")
print(student1)

student2 = Student("Jane", "Doe")
print(student2)

student3 = Student("Dane", "Joe")
print(student3)

TUD = School()
TUD.add_student(student1)
TUD.add_student(student2)
TUD.add_student(student3)
print(TUD)

print(TUD.find_student_by_id(2))

TUD.remove_student(student2)
print(TUD)

for x in TUD.students:
    print(x)
