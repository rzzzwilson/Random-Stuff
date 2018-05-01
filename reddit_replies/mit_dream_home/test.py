# MIT problem set 1

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
#return_rate = current_savings * r / 12
monthly_salary = annual_salary / 12 * portion_saved

months = 0 

while current_savings < portion_down_payment: 
    current_savings += monthly_salary + (current_savings * r / 12)
    while months % 6 == 0:
        monthly_salary = annual_salary / 12 * portion_saved * (1 + semi_annual_raise)
        break
    months += 1
    print(monthly_salary)
print("Total months: ", months)
