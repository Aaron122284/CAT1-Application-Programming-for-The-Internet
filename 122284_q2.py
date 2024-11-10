class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_grade(self, assignment, grade):
        self.assignments[assignment] = grade
        print(f"{assignment} grade set to {grade}")

    def show_grades(self):
        print(f"{self.name}'s grades: {self.assignments}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added {student.name} to {self.course_name}")

    def assign_grade(self, student, assignment, grade):
        student.add_grade(assignment, grade)

student1 = Student("Samuel", "S122284")
instructor = Instructor("Aaron", "Math 101")

instructor.add_student(student1)
instructor.assign_grade(student1, "Assignment 1", 85)
student1.show_grades()
