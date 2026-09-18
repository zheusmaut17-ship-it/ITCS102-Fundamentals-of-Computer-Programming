Sender_name = input("Enter sender name:")
item_type = input("Enter type of item:")
isFragile = input("is the item fragile? (True/False):") == "True"
weight = float(input("Enter weight (kg):"))
distance = float(input("Enter distance (km):"))
is_express = input("Is it express? (True/False):") == "True"
is_international = input("Is it international? (True/False):") == "True"

base_cost = (weight * 2.50)+ (distance * 0.15)

if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
	total = 0.00

elif is_international and is_express:
	total = (base_cost * 1.40) + 50

elif is_express or (weight > 20 and is_internatonal):
	total =(base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
	total = base_cost + 30

else:
	total = base_cost

print("\n---GLOBAL FREIGHT CALCULATOR---")
print("Sender:", Sender_name)
print("Item Type:", item_type)
print("Total Shipping Cost: $ {:.2f}".format(total))

