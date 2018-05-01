#Annual Salary
annual_salary = float(input("Enter annual salary: "))

#How much of salary will be going towards down payment
portion_saved = float(input("Enter percent of salary to save each month: "))

#Dream Home cost
total_cost = float(input("Enter cost of dream home: "))

#Raise amount
semi_annual_raise = float(input("Enter the amount of raise you expect: "))

#Down payment
portion_down_payment = 0.25 * total_cost

#Amount saved thus far
current_savings = 0

#Return of investments: This is a monthly increase
r = .04

print()

months = 0
while current_savings < portion_down_payment:
    months += 1
    if (months % 6) == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
    monthly_salary = annual_salary / 12
    savings_interest = current_savings * r / 12
    current_savings += monthly_salary * portion_saved + savings_interest

while current_savings < portion_down_payment:
    months += 1
    if (months % 6) == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
    monthly_salary = annual_salary / 12
    savings_interest = current_savings * r / 12
    current_savings += monthly_salary * portion_saved + savings_interest

print("Total months: ", months)
