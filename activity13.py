# age (integer)
# is_employed (boolen)
# credit_score (integer)
# annual_amount (float)
# has_collateral (boolen)

age = int(input("Enter age"))
is_employed = bool(input("Are you currrently employed --> "))
credit_score = eval(input("Credit Score history --> " ))
annual_income = eval(input("How much is your annual income --> "))
has_collateral = bool(input("Do you have any collateral ---> "))

if age >= 21 and is_employed == True:
     print("You are eligible for a loan")
else:
     print("Baseline requirement is failed")