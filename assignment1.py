"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""





p=float(input("Enter the initial investment: $"))
r=float(input("Enter the annual interest rate as a percentage: "))
time_type=input("Enter the time period enter (years, months, or days)")
r /= 100
time=float(input(f"Enter the length of time in {time_type}: "))
if time_type.lower() == "years":
  simple_interest = p * r * time
elif time_type.lower() == "months":
  simple_interest = p * r * (time/ 12)
elif time_type.lower() == "days":
  simple_interest = p * r * (time/ 365)

interest_earned = p + simple_interest
print(f"Your amount of earned interest is ${interest_earned: .2f}")
