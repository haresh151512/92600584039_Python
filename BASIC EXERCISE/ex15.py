#prime of not

a=int(input("Enter Number : "))
flag=0;
for i in range(2,a) :
    if a%i==0 :
        flag=1;
        break;
if flag==0 :
    print("Number is Prime")    
else :
    print("number is Not Prime")
