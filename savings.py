#The program calculates how much a person can save in a year based on their hourly income,
#hours of work, and weekly cost of living.
#We'll use variables, strings, numbers, math and printing.

#Output greet
greeting = "Hello "
name = "Carolina"
print(greeting + name)

#Calculating weekly income
hourly_wage = 17
hours_per_week = 17
income_per_week = hourly_wage * hours_per_week

#From weekly to yearly income
weeks_per_year = 48
income_per_year = weeks_per_year * income_per_week

#Yearly rent
print(name + "'s yearly income is:") 
print(income_per_year)

#Costs
spend_per_week = 250
spend_per_year = spend_per_week * 52

print(name + "'s yearly spend is:")
print(spend_per_year)

#Calculate yearly savings
savings_per_year = income_per_year - spend_per_year
print(name + "'s yearly savings:")
print(savings_per_year)