import math

#offer either investment or bond loan
print("Welcome to your financial calculator. Your calculator options are: \n\n Investment \t - to calculate the amount of interest you'll earn on your investment. \n Bond \t\t - to calculate the amount you'll have to pay on a home loan.\n")
calculation_option = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n")

#ensure capitalisation doesn't effect sorting
calculation_option = calculation_option.lower()

#separate into investment or bond loan or incorrect message using if/elif/else
if calculation_option == ("investment") :
    print("You've selected investment. Please enter the answers to the questions below:\n ")

    #User enters details to calculate investment
    amount_of_money = float(input("Please enter the amount of money you are investing:\n "))
    interest_rate_investment = float(input("Please enter the percentage interest rate (no percentage sign needed) on the investment:\n "))
    number_of_years = float(input("Please enter the number of years you plan to invest:\n "))
    interest = (input("Thank you. Is this with simple or compound interest?\n"))

    #ensuring capitlisation doesn't affect selection of interest
    interest = interest.lower()

    #Print details
    print(f"\nYou have entered the following details:\n\n Amount of money:\t\t\t {amount_of_money}\n Percentage interest rate:\t\t {interest_rate_investment}\n Number of years you plan to invest:\t {number_of_years}\n Interest:\t\t\t\t {interest}\n")

    #channel to either simple or compound interest using if/elif/else
    if interest == ("simple"):
        #Simple Interest Calculation
        total_investment_simple = amount_of_money * (1+(interest_rate_investment/100)*number_of_years)
    
        #round the value for easy viewing
        total_investment_simple = round(total_investment_simple,2)

        #print investment total
        print (f"Your calculated investment total is:\t £{total_investment_simple}\n")

    elif interest == ("compound"):
        #Compound Interest Calculation 
        total_investment_compound = amount_of_money * math.pow((1+(interest_rate_investment/100)),number_of_years)

        #round the value for easy viewing
        total_investment_compound = round(total_investment_compound,2)

        #print investment total
        print(f"Your calculated investment total is:\t £{total_investment_compound}\n")

    #invalid input answer
    else :
        print("This type of interest is not recognized. Please enter either simple or compound.")

#separated into bond calculator option
elif calculation_option == ("bond") :
    print("You've selected bond. Please enter the answers to the questions below:\n ")

    #User enter details to calculate bond
    value_of_house = float(input("Please enter the present value of the house:\n "))
    interest_rate_bond = float(input("Please enter the annual percentage interest rate (no percentage sign needed) on the bond:\n "))
    number_of_months = float(input("Please enter the number of months you plan to take to repay the bond:\n "))

    #print out details they've input
    print(f"\nYou have entered the following details:\n\n Present value of the house:\t\t {value_of_house}\n Monthly interest rate:\t\t\t {interest_rate_bond}\n Number of months you plan to invest:\t {number_of_months}\n")

   #turn interest rate into monthly interest rate for visual simplicity of calculation
    monthly_interest_rate_bond = (interest_rate_bond/100)/12

    #Calculate bond value
    total_bond_value = ((monthly_interest_rate_bond*value_of_house)/(1-(1+monthly_interest_rate_bond)**(-number_of_months)))

    #Round the value for output for easy viewing
    total_bond_value = round(total_bond_value,2)

    #Print bond value
    print(f"\nYour calculated bond repayment value is: £{total_bond_value} \n")

#invalid input answer
else:
    print("This answer is not recognized. Please try again and enter either 'Investment' or 'Bond'.")