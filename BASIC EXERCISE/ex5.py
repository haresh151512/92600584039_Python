sub1=float(input(print("Enter marks of first subject")))
sub2=float(input(print("Enter marks of second subject")))
sub3=float(input(print("Enter marks of third subject")))
total=sub1+sub2+sub3
per=total/3
print("total is: ",total)
print("persantage is: ",per)
if sub1>35 and sun2>35 and sub3>35:
    if per>35:
        print("result is: pass")
        if per>90:
            print("your class is: A")
        elif per>80:
            print("your class is: B")
        elif per>65:
            print("your class is: C")
        elif per>45:
            print("your class is: D")
        elif per>35:
            print("your class is: B")
    else:
        print("result is: fail")
else:
    print("class :your class is not alocated")
    print("result is: fail")

