#armstrong

a=int(input("Enter Number : "))
sum=0;
a1=a;
for i in range(len(a)) :
    rem=a%10;
    fact=1;
    for i in range(1,rem+1) :
        fact=fact*i;
    sum=sum+fact;
    a1=rem;
if a==sum :
    print("Number is Armstrong")    
else :
    print("number is Not Armstrong")
