name = input("Please input your name ---> ")

age = int(input("Please input your age ---> "))

if age >= 0 and age <=5  :
	print("The age is considered as INFANT ")

elif age >= 2 and age <=9  :
	print("The age is considered as EARLY CHILDHOOD ")

elif age >= 10 and age <=18  :
	print("The age is considered as ADOLESCENCE ")

elif age >= 19 and age <=30  :
	print("The age is considered as EARLY ADULTHOOD ")
else:
	print("age invalid")