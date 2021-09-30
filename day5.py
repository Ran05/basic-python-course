# Day 5 Functions 
#Creating a function 
''' 
def message(): 
 print("Hello Python") 
#Calling/Invoking a function 
message() 
#Function arguments (args) 
'''


'''
def message(name):
    print("Hi" + name)
  

message("Randolfh")

'''

'''
def message(fname, lname): 
 print(f"Hi {fname} {lname}") 
  
message("John", "Peter") 

'''


 


#Default Parameter Value 


'''
def message(name = "Mister"): #We already define the value  print(f"Hi {name}") 

    message() 

#Unknown number or Arbitrary args (*args in python #docs) 

def message(*visitors): 
 print(f"Hi {visitors[1]}") 
message("John", "Peter") 

#Keyword arguments (kwargs in python docs) 
# -we can write arguments with key=value syntax 




def message(visitor1, visitor2, visitor3): 
 print(f"Hi {visitor1}") 
 print(f"Hi {visitor2}") 
 print(f"Hi {visitor3}") #ctrl + d 
message("Don","Peter","Jake") 
'''




'''
#Arbitrary keyword arguments (**kwargs in python 
#docs) 
''' 

'''
def message(**visitor): 
 print("Hi " + visitor["fname"]) 
 print("Age is " + str(visitor["age"])) 
message(fname = "John", lname = "Depp", age = 30) 

'''
''' 
#Passing a list as an argument 
''' 

'''
def my_supplies(food): # list of strings ###############################################  for x in food: 
 print(x) 
 # print(food[2]) 
# body main part of your system 
snacks = ["fries","burger","icecream"] 
my_supplies(snacks) 

'''
'''
# Activity 1 #back at exactly 10 30 am 
# Functions with return values 
''' 

'''

def greet(): 
 return "Hello" 
x = greet() 
print(x)


'''



''' 
# simple computation using return 
''' 

'''
def compute(x, y): 
 return x*y 
# Input 
a = compute(3,5) 
print(a) 

'''


''' 
# -a function should only handle single aspect of the program # (Single responsibility principle)
# - We used docstrings(Comments to document your function) # - a function name should indicate its purpose when used
'''