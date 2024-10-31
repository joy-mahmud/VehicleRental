class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, firstname, lastname,roll):
        super().__init__(firstname, lastname)
        self.roll =roll
    def printRoll(self):
        print(f"roll:{self.roll}")


x = Person("John", "Doe")
x.printname()

studentObj=Student("joy","Mahmud",101)
studentObj.printname()
studentObj.printRoll()
