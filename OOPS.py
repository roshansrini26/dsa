print("Hello")

class family:
    father = "Srinivasan" #class sttribute
    # self parameter - ref to current instance
    def __init__(self, lname, age):
        self.lname = lname #Instance
        self.age = age

#Object
fam = family("E",48)

print(fam.father)

#single inheritance
class grandpa:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(f"grandpa's name: {self.name}")

class appa(grandpa):
    def son(self):
        print("appa is the son of grandpa")

#multilevel inheritance
class Son(appa):
    def relation(self):
        print(f"{self.name} - Rosh father")

#multiple inheritance
class mother:
    def mom(self):
        print("Padhu is mom")

class family(grandpa,mother):
    def all(self):
        print(f"{self.name} We are family")


fam = appa("ethi")
fam.display_name()
fam.son()

relative = Son("srini")
relative.display_name()
relative.relation()

rel = family("Everyone")
rel.display_name()
rel.mom()
rel.all()

#polymorphism - can have name but behave differently

#complie-time polymorphism - operator overloading
#run-time polymorphism - method overriding


#Method overriding
class Dog:
    def sound(self):
        print("Dog sound")

class Labrador(Dog):
    def sound(self):
        print("Lab woofs")

class Husky(Dog):
    def sound(self):
        print("Husky husses")

dogs = [Dog(),Labrador(),Husky()]
for f in dogs:
    f.sound()

#Method overloading
class Calculator:
    def add(self, a, b=0, c=0):
        return a+b+c
    
cal = Calculator()
print(cal.add(15,7))
print(cal.add(15,48,78))

#Encapsulation

class Family:
    def __init__(self, name, occupation, age):
        self.name = name #Public attribute
        self._occupation = occupation #Protected
        self.__age = age #Private

    def get_info(self):
        return f"Name: {self.name}, Desig: {self._occupation}, Age: {self.__age}"
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age > 15:
            self.__age = age
        else:
            print("Invalid")

obj = Family("Srini","Govt",48)

print(obj.name)

print(obj._occupation)

print(obj.get_age()) #to access private need getter and setter method

#Data abstraction - hides internal details exposing only necessary

from abc import ABC, abstractmethod

class Dog(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sound(self):
        pass

    def display_name(self):
        print(f"Dog's name: {self.name}")

class Lab(Dog):
    def sound(self):
        print("Lab woofs")

class Beagle(Dog):
    def sound(self):
        print("Beagle bark")

dogs = [Lab("Mano"), Beagle("Charl")]
for f in dogs:
    f.display_name()
    f.sound()       


    