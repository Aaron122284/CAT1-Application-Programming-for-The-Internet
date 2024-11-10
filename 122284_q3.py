class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} added to {self.department_name}")

    def total_salary(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary for {self.department_name}: {total}")

# Example usage
emp1 = Employee("Yannick", "E122284", 50000)
emp2 = Employee("Samuel", "E122285", 60000)
dept = Department("Finance")

dept.add_employee(emp1)
dept.add_employee(emp2)
dept.total_salary()
