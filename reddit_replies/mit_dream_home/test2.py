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
monthly_salary = annual_salary / 12

months = 0 
print(f'\nannual_salary={annual_salary}')
print(f'portion_saved={portion_saved}')
print(f'total_cost={total_cost}')
print(f'semi_annual_raise={semi_annual_raise}')
print(f'portion_down_payment={portion_down_payment}')

while current_savings < portion_down_payment: 
    months += 1
    current_savings += monthly_salary*portion_saved + (current_savings * r / 12)
    if months % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
    print(f'monthly_salary={monthly_salary}, current_savings={current_savings}')
print("Total months: ", months)
