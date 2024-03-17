#Program to calculate interest in various situations

#math needed for later on
import math

#while loop to check what calculator is needed
check_1 = False 

while (not check_1): 

    print("\n", "="* 25,"Calculator", "="* 25,"\n")

    choice_1 = (input("Would you like:\nInvestment or Bond?\n:").lower())

    if choice_1 == ("bond"):
        check_1 = True

    elif choice_1 == ("investment"):
        check_1 = True
    else:
        print(f"\nyour selection {choice_1} is unexpected, please try again")

if choice_1 == ("investment"):
    print("=" * 25,"Investment Calculator", "=" * 25)

#inputs to calculate below
    investment_amount = float(input("How much would you like to deposit?:"))
    investment_interest = float(input("What is the interest % ?: "))
    investment_interest_Calc = (investment_interest / 100)
    investment_length = float(input("How many years are you investing for?\n"))

#while look to see what type of interest is required below
    check_2 = False 

    while (not check_2):
        interest_type = int(input("""
For simple interest press: 1\nFor compound interest press: 2\n
"""))

        if interest_type == (1):
            check_2 = True
            interest = interest_type

        elif interest_type == (2):
            check_2 = True
            interest = interest_type

        else:
            print("Did you select correctly?")   

# user investment calculation simple & results
    if interest_type == (1): 
        interest_simple = (investment_amount *
                           (1 + investment_interest_Calc*investment_length))
        print("=" * 25, "Simple interest", "=" * 25)
        print(f"Amount invested: £{investment_amount}\t", end=" ")
        print(f"Interest at {investment_interest}%")
        print(f"Investment length: {investment_length} - years")
        print("At the end of you term you will receive £", end=" ")
        print(round(interest_simple, 2))
        print("=" * 25,"END", "=" * 25)

# user investment calculation compound & results
    if interest_type == (2): 
        interest_compound = (investment_amount * math.pow
                             ((1+investment_interest_Calc), investment_length))
        print("=" * 25, "Compound interest", "=" * 25)
        print(f"Amount invested: £{investment_amount}\t", end=" ")
        print(f"Interest at {investment_interest}%")
        print(f"Investment length: {investment_length} - years")
        print("At the end of the term you will receive £", end=" ")
        print(round(interest_compound, 2))
        print("=" * 25,"END", "=" * 25)

# request user inputs for bond calculation
else: 
    print("=" * 25,"Bond Calculator", "=" * 25)
    bond_amount = float(input("What is the value of your property?\n£"))
    bond_interest = float(input("What is the interest % ?: "))
    bond_interest_1 = ((bond_interest / 100) / 12)
    correct = False

#checker for bond length
    while (not correct): 
        bond_length = int(input("How many months do you want to repay over?:"))
        checker = (input(f"\nIs {bond_length} months correct? y/n?:").lower())
        if "y" in checker:
            correct = True

#user bond calculation & results       
    else: 
        repayment = round((bond_interest_1 * bond_amount)/
                          (1-math.pow((1+bond_interest_1),(-bond_length))), 2)
    print("=" * 25, "Bond Results", "=" * 25)
    print(f"Value of property: £{bond_amount}\t Interest at {bond_interest}%")
    print(f"The amount your need to repay each month is: £{repayment}")
    print("=" * 25,"END", "=" * 25)
