
#Activity 2 of Day 3: 


emp_Name = input("Enter employee name: ")
yrs_in_service = input("Enter years of service: ")
office = input("Enter office: ")


o = f"""
=======Bunos Form========================
"""
print(o) # divider 

if int(yrs_in_service) >= 10 and office == "it" : 
    print("Hi" + " " + emp_Name + "," + "your bunos is 10000" )

elif int(yrs_in_service) <= 10 and office == "it": 
    print("Hi" + " " + emp_Name + "," + "your bunos is 5000")

if int(yrs_in_service) >= 10 and office == "acct" : 
    print("Hi" + " " + emp_Name + "," + "your bunos is 12000" )

elif int(yrs_in_service) <= 10 and office == "acct": 
    print("Hi" + " " + emp_Name + "," + "your bunos is 6000")

if int(yrs_in_service) >= 10 and office == "hr" : 
    print("Hi" + " " + emp_Name + "," + "your bunos is 15000" )

elif int(yrs_in_service) <= 10 and office == "hr": 
    print("Hi" + " " + emp_Name + "," + "your bunos is 7500")

output = f"""
========================================
"""
print(output) # divider