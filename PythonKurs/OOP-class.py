# class

class Person:
    #pass kelimesi yer tutucu görevinde
    # class attributes
    adress= "no information"

    # constuctor(yapıcı metot)
    def __init__(self, name, year):
        #object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı")

    #methods
    def intro(self):
        print(f"hello there. i am {self.name}")

    def calculateAge(self):
        return 2024-self.year


#object (instance)
p1 = Person("ali",1990)
p2 = Person("ayça",2012)

#updating
p1.name="Veli"
p1.year=2000
p1.adress="mersin"

#accessing object attributes
print(f"p1--> name:{p1.name}, year:{p1.year}, adress:{p1.adress} ")
print(f"p2--> name:{p2.name}, year:{p2.year}, adress:{p2.adress} ")
print(p1)
print(p2)
print(type(p1))
print(type(p2))

p1.intro()
p2.intro()

print(f" yaşım {p1.calculateAge()}")



class Circle:
    #class attibute
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    def cevreHesapla(self):
        return 2*self.pi*self.yaricap

    def alanHesapla(self):
        return self.pi*(self.yaricap**2)


c1 = Circle()     #yaricap 1
c2 = Circle(5)

print(f" c1 alan: {c1.alanHesapla()} , c1 cevre : {c1.cevreHesapla()}")
print(f" c2 alan: {c2.alanHesapla()} , c2 cevre : {c2.cevreHesapla()}")