# age (integer)
# is_employed (boolen)
# credit_score (integer)
# annual_amount (float)
# has_collateral (boolen)
# Loan and Collateral System


# Collateral Loan System
# College Student Project

print("================================")
print("     COLLATERAL LOAN SYSTEM")
print("================================")

# Login
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":

    print("\nLogin Successful!")

    # Borrower Information
    name = input("\nEnter your name: ")
    age = int(input("Enter your age: "))

    if age <= 65 and age > 0:

        # Collateral Information
        print("\n--- Collateral Information ---")

        collateral = input("Enter collateral (motorcycle, land, house): ")
        value = float(input("Enter collateral value: "))

        if value >= 30000:

            # Loan Information
            print("\n--- Loan Information ---")

            loan = float(input("Enter loan amount: "))

            if loan > 0 and loan <= value:

                # Interest Calculation
                rate = 0.10
                interest = loan * rate
                total = loan + interest

                # Display Result
                print("\n================================")
                print("          LOAN SUMMARY")
                print("================================")

                print("Name:", name)
                print("Age:", age)
                print("Collateral:", collateral)
                print("Collateral Value: PHP", value)
                print("Loan Amount: PHP", loan)
                print("Interest Rate:", rate * 100, "%")
                print("Interest: PHP", interest)
                print("Total Payment: PHP", total)

                print("\nLoan Application Complete!")

            else:
                print("Invalid loan amount!")

        else:
            print("Collateral value must be at least PHP 30,000.")

    else:
        print("Maximum age is 65 years old.")

else:
    print("Invalid username or password!")
    
age = int(input("Enter age"))
is_employed = bool(input("Are you currrently employed --> "))
credit_score = eval(input("Credit Score history --> " ))
annual_income = eval(input("How much is your annual income --> "))
has_collateral = bool(input("Do you have any collateral ---> "))

if age >= 21 and is_employed == True:
     print("You are eligible for a loan")
else:
     print("Baseline requirement is failed")