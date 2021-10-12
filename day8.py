# Defining a class using the keyword class ----- T1
'''
class Dog:
    name = "Bandog" #Fields
    breed ="Chow chow" #Fields


class MyNumber:
    x = 5



# Creating an object (instantiation) ----- T2


# Ex ----- E1


p1 = Dog() #we instantiate an object p1


print(p1.name)# Output
print(p1.breed)# Output
'''




'''
-an object of a class will have the
variables (properties) and methods (behavior)
defined in that class  
'''


# Ex ----- E2
'''
class MyNumber:
    x = 5


p2 = MyNumber() #we instantiate another object p2
print(p2.x)
'''




# !!!!!!!!!!




# Ex ----- E3
'''
class MyNumber:

    # Class Body
    x = 0 # Fields





# Instantiation
p1 = MyNumber()
p2 = MyNumber()


p1.x = 5 # Change the given Attributes


# Printing
print(p1.x)
print(p2.x)
'''









# Activity 1











# The __init__() function for class instantiation ----- T3


# !!!!!!!!!!

# Ex ----- E4
# Adding value
'''
class Dog:
  def __init__(pangDog, name, breed):
    pangDog.name1 = name
    pangDog.breed1 = breed


userIn1 = input("Name:")
userIn2 = input("Breed:")

d1 = Dog(userIn1, userIn2) # Value that you defined in your fields
# d1 = Dog(userIn1, userIn2)


print(d1.name1)
print(d1.breed1)
'''



# !!!!!!!!!!







# Activity 2










# Methods (class behaviors) ----- T4

# !!!!!!!!!!

# Ex ----- E5
'''
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(barkSelf):
      print ("Bow wow wow!")
      print(f"Name: {barkSelf.name}, Breed: {barkSelf.breed}")


d1 = Dog("papi","chihuahua")

d1.bark()


'''



# Ex ----- E6
'''
class Person:
  def __init__(self, fname, lname, n1, n2):
    self.firstname = fname
    self.lastname = lname
    self.nn1 = n1
    self.nn2 = n2

  def magCompute(comPute):
      return comPute.nn1+comPute.nn2

  def printName(paraSaPrint):
    print(paraSaPrint.firstname, paraSaPrint.lastname)


x = Person("John", "Doe",1 ,2) #creates a Person object x


x.printName()             #object x calls the method printname
print(x.magCompute())
'''



# Access modifiers
'''
-Python uses ‘_’ symbol to determine the access 
control for a specific  data member or a member 
function of a class.
-Access specifiers in  Python have an important 
role to play in securing data from  unauthorized 
access and in preventing it from being exploited.
'''

# Public access
'''
-The members of a class that are declared public 
are accessible from any part of the program. 
-All data members and member functions of a class 
are public by default.
'''


# By Default Public Access

'''

class Dog:
  color = "Black"
  def __init__(self, name):
    self.name = name

  def bark(self):
      print (f"Bow wow wow! ako ay '{self.color}'")

  def Jump(self):
      print (f"Up Up! ako ay '{self.color}'")

# creating another class to access Public variable
class Trix:
    def Kulay(self):
        print("Hello")


dogObj = Dog("Bandog")
trixObj = Trix()

print(dogObj.color) #access the public variable

# print(dir(dogObj)) #to see if your modifiers are public, private or protected

# dogObj.bark()
# dogObj.Jump()


trixObj.color = "Blue"

print(trixObj.color)
'''


# Private access
'''
-The members of a class that are declared private 
are accessible within the class only 
-private access modifier is the most secure access modifier 
-members of a class are declared private by adding a 
double underscore ‘__’ symbol before their names
'''

# ex 1
"""
class Student:
    __schoolName = 'Trix School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute


    def __display(self):  # public method kaya maaccess naten yung output nya
        print(self.__name) # The process must be inside
        # print("This is Private")


'''
std = Student("Trix", 25)
'''

# print(dir(std)) #to see if your modifiers are public, private or protected
# print(std.__schoolName)


# print(std._Student__schoolName)



# std.display()
'''
std._Student__display() #accessing methods in private
'''

"""




# ex 2
'''
class Dog:

  def __init__(self, name, breed):
    self.__name = name
    self.__breed = breed

  def bark(self):
      print ("Bow wow wow!")
      print(self.__name)

  def setName(lagayPangalan, newname):
      lagayPangalan.__name = newname

  def getName(kuhaPangalan):
      return kuhaPangalan.__name


d1 = Dog("papi","bulldog") #Instantiation


# d1.bark() #We can also define value in methods in one class



d1.setName("toti") #We can also define value in methods in one class
print(d1.getName())
'''






# Protected access
'''
-members of a class that are declared protected 
are only accessible to a class derived from it
-members of a class are declared  protected by adding 
a single underscore ‘_’ symbol before their names
'''


'''
class Animal:  #Parent Class
    _type = ""

    def _eat(self):
        print("Eating...")

#ChildClass 1
class Dog(Animal):
  def __init__(self, name, breed):
    self.__name = name
    self.__breed = breed
    self._type = "mammal"


#ChildClass 2
class Snake(Animal):
    def __init__(self):
        self._type = "vertebrae"


dogObj = Dog("Bandog", "Bulldog")
snakeObj = Snake()

# print(dir(dogObj)) #to see if your modifiers are public, private or protected


print(dogObj._type)
print(snakeObj._type)

'''






# Activity 3
