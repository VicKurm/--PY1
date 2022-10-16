money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
spend = salary - (salary-spend)
while money_capital >= spend:
    spend = spend*(1+increase)
    month += 1
spend = spend * (1+increase)

print(month)
