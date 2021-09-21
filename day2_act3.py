

# Activity number 3 on day 2 09-21-21

emp_Name = str(input("Enter Employee Name: "))
num_Hours = float(input("Enter number of hours: "))
sss_cont = float(input("SSS Contribution:"))
philHealth_cont = float(input("Philhealth Contribution:"))
rate_per_hour = int(500)
gross_salary = num_Hours * rate_per_hour
tax = float(500.00)
total_deductions = gross_salary - sss_cont -philHealth_cont - tax


output = f"""
=================PAYSLIP=================
==========EMPLOYEE INFORMATION===========

"""
print(output)
print("Employee Name: " + emp_Name)
print("Rendered Hours:" + str(num_Hours))
print("Rate Per Hour: " + str(rate_per_hour))
print(gross_salary)

output2 = f"""
=================Deductions=================

"""
print(output2)
print("SSS: " + str(sss_cont))
print("Philhealth:" + str(philHealth_cont))
print("Tax:" + str(tax))
print("Total Deductions: " + str(total_deductions))

