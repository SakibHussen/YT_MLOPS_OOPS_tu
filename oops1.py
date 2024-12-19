#initiate a class
class Employee:
    #special method
    def __init__(self, name, id, salary, dep):
        self.name = name
        self.id = id
        self.salary = salary
        self.dep = dep
    def travel(self,destination):
        print(f"{self.name} is traveling to {destination}")


    
    

#Creating an object of this class
emp1 = Employee("Rahul", 101, 50000, "HR",)
emp1.travel("Sylhet")

print(emp1.name)