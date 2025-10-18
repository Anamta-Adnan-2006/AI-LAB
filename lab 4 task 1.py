class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Job:
    def __init__(self, designation, salary):
        self.designation = designation
        self.salary = salary
class Employee(Person, Job):
    def __init__(self, name, age, designation, salary):
        Person.__init__(self, name, age)
        Job.__init__(self, designation, salary)
    def display_details(self):
        print("----- Employee Details -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Designation:", self.designation)
        print("Salary:", self.salary)
emp1 = Employee("Anamta adnan", 19, "cyber security", 85000)
emp1.display_details()
