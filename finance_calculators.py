"""
This is a finance calculator program, which calculates the amount of interest on 
an investment and the amount of monthly repayment on a home loan based on user entries.
When calculating investment interest a user can choose between simple or compound interest options.
"""

import math

print(11*'=' + "FINANCE CALCULATORS" + 50*'=')
print()
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on the home loan")
print(80*'=')

#The user chooses which calculator is preferred: "investment" or "bond".

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if choice == "investment":
    print(f"Your choice is: {choice}")
    print(80*'=')
    money = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter your interest rate: "))/100
    years = float(input("Enter number of years you plan on inversting: "))
    print()
    interest = input("Do you want 'simple' or 'compound' interest?: ").lower()
    print(f"Your choice is: {interest}")
    print(80*'=')
    print("Here is the answer based on your entries: ")
    print()
#User chosen "investment" calculator and now must pick what type of interest is required "simple" or "compound"
#Next, depending on the type of interest, the program calculates the final result of the total interest earned
    
    if interest == "simple":
        total_simple = money * (1 + interest_rate * years)
        print(f"After {int(years)} years at interest rate {round(interest_rate*100,2)}% you will earn total of £{round(total_simple,2)}")
        print()
    elif interest == "compound":
        total_compound = money * math.pow((1 + interest_rate), years)
        print(f"After {int(years)} years at the interest rate {round(interest_rate*100,2)}% you will earn total of £{round(total_compound,2)}")
        print()
    else:
        print("Error: Wrong Entry! Enter either 'simple' or 'compound'")

#If a user chooses "bond" calculator the program calculates the monthly repayment amount on a home loan.                    
elif choice == "bond":
    print(f"Your choice is: {choice}")
    print(80*'=')
    
    house_value = float(input("Enter present value of the house: "))
    interest_rate = (float(input("Enter your interest rate: "))/100)/12
    months_to_repay = int(input("Enter number of months to repay the the bond: "))
    repayment = (interest_rate * house_value)/(1 - (1 + interest_rate)**(-months_to_repay))

    print(80*'=')
    print("Here is the answer based on your entries: ")
    print()
    print(f"You will have to repay £{round(repayment,2)} each month on your home loan.")
    print()

else:
    print("Error: Wrong Entry! Enter either 'investment' or 'bond'")

print(80*'=')
print("**Thank you for choosing our calculator!**")
