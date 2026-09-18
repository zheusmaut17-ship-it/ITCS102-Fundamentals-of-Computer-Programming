import getpass

username = "zheus"
passowrd = "bosengwalangkain"

u = input("INPUT USERNAME ---> ")
p = getpass.getpass("INPUT PASSWORD ---> ")


if u == username :
	print("username correct")

else:
	print("username incorrect")

if p == passowrd:
	print("passowrd correct")

else:
	print("passowrd incorrect")