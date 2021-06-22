class Employee:
    company = 'Google'
    def getSalary(self):
        print (f'Salary for {self.name} working in {self.company} is {self.salary}')

nirmit = Employee()
nirmit.name = 'Nirmit'
nirmit.salary = 100000
nirmit.getSalary()
# Employee.getSalary(nirmit)
# actually nirmit.getSalary() converts to Employee.getSalary(nirmit) in machine point of view
