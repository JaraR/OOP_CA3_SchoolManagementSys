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


# Main Program
student1 = Student(1, "John", "Doe")
print(student1)
