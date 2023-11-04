class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name

class Student(Person):
    def _init_(self, std_name, std_age, std_rollnumber):
        super()._init_(std_name, std_age)
        self.roll_number = std_rollnumber
        self.std_courses = []
    def register_for_course(self, course):
        self.std_courses.append(course)

class Instructor(Person):
    def _init_(self, inst_name, inst_age, salary):
        super()._init_(inst_name, inst_age)
        self.salary = salary
        self.inst_courses = []
    def assign_course(self, course):
        self.inst_courses.append(course)

class Course:
    def _init_(self, course_id, name):
        self.id = course_id
        self.name = name
        self.students = []
        self.instructors = []
    def add_student(self, student):
        self.students.append(student)
    def set_instructor(self, instructor):
        self.instructors.append(instructor)