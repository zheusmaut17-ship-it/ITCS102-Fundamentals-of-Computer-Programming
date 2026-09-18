name = input("please input your name--->")
age = int(input("Please input your age--->"))

if age >= 0 and age <= 3:
	print("That age are considered as Infant")

elif age >= 4 and age <= 12:
	print("That age are considered as Child")

elif age >= 13 and age <= 19:
	print("That age are considered as Adolecent")

elif age >= 20 and age <= 39:
	print("That age are considered as Young adult")

elif age >= 40 and age <= 59:
	print("the age are considered as Middle age adult")

else:
	print("Too Old can't defined")