# Challenge: Employee class
# Static and instance variable

class Employee:
    """Class contains employee details"""

    employee_count = 101

    def __init__(self, emp_name, emp_desg, emp_sal):
        self.e_name = emp_name
        self.e_sal = emp_sal
        self.e_desg = emp_desg
        self.e_id = "e" + str(Employee.employee_count)
        Employee.employee_count += 1

    def __str__(self):
        """Prints the string representation of object"""
        return f"\tEmployee Details:\nID: {self.e_id}\nName: {self.e_name}\nDesg.: {self.e_desg}\nSalary: {self.e_sal}"

    @classmethod
    def total_employees(cls):
        """Calculates the employee count."""
        return Employee.employee_count - 101


e1 = Employee("John", "Engineering Manager", 100000)
print(e1)
# print(e1.total_employees())

# creating another employee
e2 = Employee("Julius", "Team Lead", 1222230)
print("\n")
print(e2)
print("\n")
print(f"Total employees: {Employee.total_employees()}")
