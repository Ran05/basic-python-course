# Day 2

#Basic string operation

#Displaying

# Note



# print('John said "I don\'t like vegetables"') \ it is use for escape character
# print("Mike said 'I love eating burger!' ") 
# print("This next text will move to the \nnext line") \n for a new line 

# print("\t\t\t\tThis text comes after a tab")





#######
##########

# TOPIC: BASIC STRING OPERATION

##################


''''
a = "Hellow World"
print(a)

'''

'''
name = input("Enter a name: ")
print(name)


'''


#accessing string elements

'''

a = "Hello World"
print(a)

print(a[10])
'''


# Multiline string


'''
a ="""Hello World,
Hello Python!
"""
print(a)
'''

#Looping through string elements

'''
for x in "banana":
    print(x) #
print(x)
'''

# STRING PLACEHOLDERS

# Placeholder, the use of {} format


'''
name = "John"
food = "Rice"
game = "cheese"


sampleText1 = "My name is {} I love {} and playing {}"

sampleText1a = sampleText1.format(name,food,game) 

print(sampleText1a)


# other example

# sampleText2 = "My name is {2} I love {1} and playing {0}".format(name,food,game)
'''


# other example
'''
name = "John"
food = "Rice"
game = "cheese"

sampleText2 = "My name is {2} I love {1} and playing {0}".format(name,food,game)
sampleText2a = sampleText2.format(name,food,game) # 

print(sampleText2)
'''

'''
sampleText3 = "My name is {newname} I love {newfood} \
and playing {newgame}"

sampleText3a = sampleText3.format(newname="Mike", newfood="burger", newgame="volleyball")

print(sampleText3a)
'''


#place holder, the use of %
'''
num = 2
item = "milk"
cost = 35.50

sampleText4 = "The product %s with item no. %d costs %.d" %(item,num,cost)

print(sampleText4)

'''


#placeholder, the use of f{}

'''
item = "milk"
quantity = 5
cost = 35.50

price = cost * quantity

sampleText5 = f"The product {item} costs {price} pesos"

# other example

# print(f"The product {item} costs {cost*quantity} pesos.")


print("The product" + item + "costs" + str(price) + "pesos." )





print(sampleText5)


'''



#

output = f"""
        =======
        Name   Age
        =======
        xxxxxxxxxxxxxx
"""

print(output.format())




#String manipulation
'''
s = "Hello, World!"

print(s[2:6]) #counted na ang zero 

'''

#####
#######Negative indexing, starts the slice from the end


'''
s = "Hello, World!"

print(s[-5:-2])
'''




#####
###### STRIPING (tatangalin niya ang whitespace) 
########

'''
s = "    Hello, World!          "

print(s)

print(s.strip())

'''
#####
# ##### String length
##########
#note
'''
s = "Hello, World!"
print(len(s))
'''

###### STRING FORMATTING ######

#string upper
'''
s = "Hello World!"

print(s.upper())
'''


#string lower
'''
s = "Hello World!"

print(s.lower())

'''




#string Capitalize 
'''
s = "philippines"

print(s.capitalize())
'''



#String title
'''
s = "this is a journal paper title"

print(s.title())
'''

# Activity 1 





### Split(), splits the string with the specified separator #####

'''
s = "Welcome to Python Programming"

s1 = "Hello, my name is John, I am doing Python."

x = s1.split(',',3)
print(x)
'''


s = "I like playing basketball basketball"
x = s.replace("basketball", "football", 1). replace("like","football")

print(x)


'''
txt = "He who plants a tree plants a hope!"

'''


### Number Formatting Functions #######


# import math 

# grade1 = 95.50
# grade2 = 95.20 


# print(round(grade1,1))

# print(math.ceil(grade1))
# print(math.ceil(grade2))
# print(math.floor(grade1))
# print(math.floor(grade2))


# print(pow(2,3))
# print(2**3)






 



