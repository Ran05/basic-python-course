



# if statement
'''
a = 40000
b = 510

if a > b:
    print(f"{a} is greater than {b}")

print("Testing control structures")

'''

# if else 
'''

a = 555
b = 555

if a > b:
    print(f"{a} is greater than {b}")

elif a >=b:
    print(f"{a} is greater than {b}")
'''



# else statement

'''

a = 555
b = 5500

if a > b:
    print(f"{a} is greater than {b}")

elif a >=b:
    print(f"{a} is equal to {b}")

else:
    print(f"{b} is less than {a}")
'''



# Shorthand if and if-else 

#1st format
'''
a = 555
b = 5500

if a > b: print(f"{a} greater than {b}")
elif a==b: print(f"{a} is equal to {b}")
else: print(f"{b} is less than {a}")

'''


#Ternary operator 



'''
a = 555
b = 5500

print("A is greater than B") if a > b else print("B is greater or equal to A") #mas paiikliliin niya ang code unlike sa mga naunang sample

'''


'''
a = 4
b = 4

if a > b: 
    print("A")

elif a==b:
    print("=")

else: 
    print("B")

'''

#Nested if 

'''
x = 11

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

else: print("Not above ten")
'''

#Compounding operations

'''
a = 2000
b = 1200
c = 50


if a > b or c > a: 
    print("A condition is true....")
else : print("A condition is not true")

'''


'''
a = 200
b = 1200
c = 50


if a > b and c > a: 
    print("Both condition are true....")
else : print("Both condition are not true")


'''

# x = input()

# if x.isalpha():
#     print("x is an alphabet")

# if x.isalnum():
#     print("x is alphanumeric")


# if x.islower():
#     print("YEs this is the lower")
# else: print("Not in a lower case")


# if x.isupper():
#     pass # nothing will do ito mag papass lang siya   
#     print("YEs this is the upper")
# else: print("Not in a  upper")


####### PRINT STATEMENT #########


a =30
b=20

if b > a:
    pass
elif a > b:
    print("Hello")