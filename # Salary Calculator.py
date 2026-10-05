#Question 6
# Salary Calculator

basic_salary = float(input("Enter your basic salary: ₹"))

hra = basic_salary * 0.20
da = basic_salary * 0.10

gross_salary = basic_salary + hra + da

deduction = basic_salary * 0.05

net_salary = gross_salary - deduction

print("\n--- Salary Details ---")
print("Basic Salary :", basic_salary)
print("HRA (20%)    :", hra)
print("DA (10%)     :", da)
print("Gross Salary :", gross_salary)
print("Deduction    :", deduction)
print("Net Salary   :", net_salary)