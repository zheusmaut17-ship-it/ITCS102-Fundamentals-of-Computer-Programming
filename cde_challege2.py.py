money = eval(input("Enter Money to Deposit ---->>> ")) # int(), eval()
print(type(money))
print("=*=-=*=-=*=>> PH BANK DENOMINATION <<=*=-=*=-=*=")
print(" MONEY TO DEPOSIT ---------------->. ", money, "ph")

a = money// 10000
money = money % 10000
b = money// 5000
money = money % 5000
c = money// 1000
money = money % 1000
d  = money// 500
money = money % 500
e = money// 200
money = money % 200
f = money// 100
money = money % 100
g = money// 50
money = money % 50
h = money// 20
money = money % 20
i = money// 10
money = money % 10
j = money// 5
money = money % 5
k = money// 1
money = money % 1
print("\n\n10000 =",a)
print("5000 =",b)
print("1000 =",c)
print("500 =",d)
print("200 =",e)
print("100 =",f)
print("50 =",g)
print("20 =",h)
print("10 =",i)
print("5 =",j)
print("1 =",k)

print("\n\n=*=-=*=-=*=>> END OF BREAKDOWN <<=*=-=*=-=*=")