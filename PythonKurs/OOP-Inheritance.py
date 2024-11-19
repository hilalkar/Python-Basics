# Inheritance (Kalıtım) = Miras Alma
from idlelib.colorizer import prog_group_name_to_tag
from traceback import print_tb


class Person():
     def __init__(self,fname, lname):
         self.firstname=fname
         self.lastname=lname
         print("person created")

     def who_am_i(self):
         print("I am a person")
     def eat(self):
         print("I am eating")

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)    #person özelliklerini kullanmak için çağırdık
        print("student created")

    #override
    def who_am_i(self):
        print("I am a student")

p1 = Person("ali","turan")
s1 = Student("asım","akça")

print(p1.firstname+ " "+ p1.lastname)
print(s1.firstname+" "+ s1.lastname)

p1.who_am_i()
s1.eat()

class Teacher():
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch

    def who_am_i(self):
        print("I am a Teacher")
