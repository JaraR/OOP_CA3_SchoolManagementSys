class Student(object):
    """student class that is then inherited by English, History, and Math student class"""

    def __init__(self, student_id, first, last):
        """initializes a student with an ID, first name, and last name"""
        self.student_id = student_id
        self.first = first
        self.last = last

    def __str__(self):
        """returns a student's ID, first name, and last name"""
        return "ID: " + str(self.student_id) + " Name: " + self.first + " " + self.last


class EnglishStudent(Student):
    """English student class that inherits from student class"""

    def __init__(self, student_id, first, last, english_grade):
        """initializes an English student with an ID, first name, last name, and an English grade"""
        Student.__init__(self, student_id, first, last)
        self.english_grade = english_grade

    def __str__(self):
        """returns a student's ID, first name, last name, and English grade"""
        result_str = Student.__str__(self)
        result_str = result_str + " English grade: " + str(self.english_grade)
        return result_str


class HistoryStudent(Student):
    """History student class that inherits from student class"""

    def __init__(self, student_id, first, last, history_grade):
        """initializes a History student with an ID, first name, last name, and a History grade"""
        Student.__init__(self, student_id, first, last)
        self.history_grade = history_grade

    def __str__(self):
        """returns a student's ID, first name, last name, and History grade"""
        result_str = Student.__str__(self)
        result_str = result_str + " History grade: " + str(self.history_grade)
        return result_str


# Main Program
student1 = Student(1, "John", "Doe")
print(student1)
