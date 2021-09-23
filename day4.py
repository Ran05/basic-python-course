

#Day 4 

#### While loop ####
'''

a = 1

while a < 6:
    # (loop exit condition)
    print(a)
    a += 1

'''

######## Break statement #########
'''
a = 1
while a < 6:
    print(a)
    if a==2:
        print("Hello")
        break
    a += 1

'''




####### Continue statement 
'''

a =1 
while a < 6:
    if a == 3:
        a += 1
        continue 
    print(a)
    a+=1
    
'''


#else statement in while
'''

a = 1
while a <=6:
    print(a)
    a+=1 # iteration
else:
    print("a is no longer less than 6")

'''


# For Loop 


# a =1

# for a in range (0,10,2):
#     print(a)

#syntax : range(start, stop,step)


########### Looping through string ##################


'''
for x in "banana" : 
    print(x)

'''

'''

for x in "banana" : 
    if x == 'n':
        break 
    print(x)
'''


############### Arithmetic operations + - / * % ###########

'''
a = int(input(""))

if a%2 == 0:
    print("a is divisible by 2")
else: print("a is not divisible by 2")

'''


# print("*" * "20" ) #instead of looping a character




######################### List #################################

'''
numbers = [1,2,3,4,5,6]

print(numbers[1])
'''
'''
food = ["cake", "burger" , "Fries"]

print(food)
print(type[food])

'''



# food = ["cake", "burger" , "Fries"]
# print(food[-2])

# Python list may contain different types

'''
mixed_list = ["mike", 1,2, "John", 2.5, True]

print(type(mixed_list[4]))

'''
####################### Looping through list elements ##########################

'''

names = ["mike", "ana", "jun"]

for name in names:
    print(names)

'''

# List Handling methods

'''
thisList = ["dog", "Cat", "Mouse" ]

print(len(thisList))


'''
####################### Adding elements to a list #########################

#append() magdagdag ito ng data sa array

'''
numList = [1,2,3,4,5]
numList.append(99) # idadagdag ito sa last index ng array


print(numList)

'''


######################## Inserting elements to a list ##########################

# Insert mas control mo ito unlike sa append na ilalagay niya lang sa dulo.

'''
male = ["John", "mike"]

male.insert(3,"Jake")

print(male)

'''



'''
male = ["John", "mike", "Jake"]

male.remove("Jake")

print(male)


'''

# pop aalisin niiya ang data from array


'''
male = ["John", "mike", "Jake"]

male.pop()

print(male)

'''


# 3rd way
'''
male = ["John", "mike", "Jake"]

del male[1]

print(male)





######


'''

'''

male = ["John", "mike", "Jake"]

male.clear()

print(male)


'''



 
# Arranging 
'''

numList = [20, 2, 33, 42,25]
numList.sort(reverse=True)
print(numList)


numList = [20, 2, 33, 42,25]
numList.sort()
print(numList)


'''


#String Sorting
# reverse() irereverse niya ang data sa array

'''
fruitList = ["orange", "Mango", "Kiwi", "Banana"]

fruitList.sort()


print(fruitList)


'''

#COunt - bibilangin niya ang same data sa array/
'''

numList= [25,2,33,42,25,"25"]

counter = numList.count(25)

print(counter)

'''
#### index() -- hahanapin niya kung saang index position ang data ##########

'''
numList= [25,2,33,42,25,]


indexPosition = numList.index(42)

print(indexPosition)

'''


######## Copying List #########
'''

fruits1 = ["apple", "banana", "cherry"]
fruits2 = ["mango", "coconut", "dragon fruit"]


# myList = fruits2.copy() + fruits2.copy()
myList = fruits2 + fruits2

print(myList)

'''

# USing list() function for conversion


'''
fruits1 = ["apple", "banana", "cherry"]
fruits1 = ["apple", "banana", "cherry"]
fruits1 = ["apple", "banana", "cherry"]

mylist = list(fruits1)

print(mylist)







male = ["bien","john"]
female = ["jayde", "ana"]
for x in female:
    male.append(x)
print(male)


'''





# List comprehension techniques


'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = []

for x in fruits:
    if "banana" in x:
        newList.append(x)
    elif "cherry" in x:
        newList.append(x)
print(newList)

'''

'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


# newlist  = [x for x in fruits if "a" in x]

# newlist  = [x for x in fruits]

# newlist = [x for x in fruits if x !="mango"]


# print(newlist)


'''

# Activity # 2


