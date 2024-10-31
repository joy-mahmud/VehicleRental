class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

  def printNameAndAge(self):
      return (f"name:{self.name},age:{self.age}")

  def profession(self,job,salary):
      self.job = job
      self.salary = salary
      print(f"job:{self.job}, salary:{self.salary}")
      print(self)
      return self


class new_class:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(num1,num2)

    def my_method(self):
        print("This is from new class ")

p1 = Person("John", 36)
print(p1.printNameAndAge())
p1.profession("teacher",20000)
prof=p1.profession("singer",10000)
print(prof.job)

print(p1.name)
print(p1.age)
p2=Person("joy",27)

newcls = new_class(5,10)
print(newcls.num1)
# newcls.my_method()
# print(newcls.num1,",", newcls.num2)
# newcls.num1=20
# print(f"num1:{newcls.num1}")

newclas2=new_class(30,40)
print(newclas2.num1)
