no1=float(input(print("Enter first number")))
no2=float(input(print("Enter second number")))
no3=float(input(print("Enter thard number")))
if no1==no2==no3:
    print("all are same number")
elif no1>no2 and no1>no3:
    print(no1," is biger than ",no2," and ",no3)
elif no2>no1 and no2>no3:
    print(no2," is biger than ",no1," and ",no3)
elif no3>no2 and no3>no1:
    print(no3," is biger than ",no1," and ",no2)
elif no1==no2 and no1>no3:
    print(no1," and ",no2," is biger than ",no3)
elif no2==no3 and no2>no1:
    print(no2," and ",no3," is biger than ",no1)
else:
    print(no1," and ",no3," is biger than ",no2)
