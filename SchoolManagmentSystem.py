class Student(object):
    def __init__(self, ID, first, last):
        """initializes a student with an ID, first name, and last name"""
        self.ID = ID
        self.first = first
        self.last = last

    def __str__(self):
        return "ID: " + str(self.ID) + " Name: " + self.first + " " + self.last


student1 = Student(1, "John", "Doe")
print(student1)
