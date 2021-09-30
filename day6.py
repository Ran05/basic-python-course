
#list 
#ordered, changeable and also allow duplicates

'''
tup1 = ('physics', 'chemistry',1997,2000)

print(tup1)


tup2 = (1,2,3,4,5)
print(tup2)

tup4 = tuple(('maths','science','english'))

print(type(tup4))



'''


'''

tup2 = (1,2,3,4,5,1,2)

# print(tup2[5])
print(tup2[1:5])


'''

'''

my_tuple = ("only_item")
print(type(my_tuple))
'''


#Defining variables

'''

t = (1,2,3)
t1 = list(t)
t1[2] = 5 

t1[2] = 5
print(type(t1))

'''


# Accessing tuples using for loop

'''
t = (1,2,3)
t1 = list(t)

t = t1.copy()
for i in t:
    print(i)
'''


#normal printing of tuples

'''
t = (1,2,3)
t1 = list(t)

t = t1.copy()

print(t)

'''


### Dictionary ####


#Defining variables 1st way

'''
dict = {'Name': 'Zara',
 'Age': 7,
'Class': 'First'}

print(dict)


'''


#Duplicate Variables 2nd way

'''
dict = {'Name': 'Zara',
 'Age': 7,
'Class': 'First'}

dict = ['Age'] = 10
print(dict)

'''




#Adding new entries 


'''
dict = {'Name': 'Zara',
 'Age': 7,
'Class': 'First'}

dict["Address"] = "Zamboanga City"


print(dict)


'''




'''
dict = {'Name': 'Zara',
 'Age': 7,
'Class': 'First'}


dict.popitem()
print(dict)
'''




# dict = {'Name': 'Zara',
#  'Age': 7,
# 'Class': 'First'}


# del dict ['Name']

# dict.clear()
# print(dict)





###=============================================


'''
remDict = {
    "brand": "Yamaha",
    "model": "mio",
    "year": "2016",
}

# del remDict
print(remDict)


'''


##==========================================


#Sets

#examples


'''
fruits = {"apple" "banana", "cherry"}
numbers = {1,2,3,4,5}
booleans = {True,False,False}

mixed = {"apple",1, True,"banana"}

print(booleans)

'''


###========== Adding items in set =======

'''

fruits = {"apple" "banana", "cherry"}

fruits.add("Mango")
print(fruits)


'''

'''
prog = {"C", "C#", "Java"}

prog.update("PHP", "Js")


print(prog)

'''


# -================= USing the constructor set ==========

# my_list(1,2,3,4,5,3,2,1)

# myset = set(my_list)





#=================Checking elements in sets 


'''


mySet = {"apple", "banana", "cherry"}

print("Cherry" in mySet)

'''

#====== removing Sets
# Using remove

'''
mySet = {"apple", "banana", "cherry"}

mySet.remove("cherry")

print(mySet)
'''



# myTuple =("apple")
# print(type(myTuple))



# my_givin = [10,12,12,3,4,12,14,4]

# my_output = set(my_givin)

# print(type(my_givin))





########### ======================== ################


#MODULES: 

#pre-define functions


# python built-in modules

#DATE: TIME: 

'''

import datetime
x =datetime.datetime.now()
print(x)

'''

# built in math modules


'''
import math 
x=math.sqrt(64)
y =math.pi
print(x)
'''


#list all functions names in module,

'''
dir()
import math 

x = dir(math)
print(x)

'''


