
# Day 3 of DICT PYTHON COURSE - ACTIVITY #1



name = input("Enter your name: ")
mathGrade = input("Enter your math grade: ")
scieGrade = input("Enter your science grade: ")
engGrade = input("Enter your english grade: ")



sum = float(mathGrade) + float(scieGrade) + float(engGrade) 
average = sum / 3

output = f"""
================RESULT=====================
"""

print(output)

print("Your average is"+ " " + str(round(average)))

if average >= 75:
    print("Congratulations" +" "+ name + " you are passed!") 
    if float(mathGrade) <= 75:
     print("But you need to re-enroll Math subject")
    if float(scieGrade) <= 75:
     print("But you need to re-enroll Science subject")
    if float(engGrade) <= 75:
     print("But you need to re-enroll English subject")
elif average <= 75:
    print("Sorry, You failed the semester ")


    

