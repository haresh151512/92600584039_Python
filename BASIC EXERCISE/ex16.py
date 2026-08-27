#Krishnamurti

a=int(input("Enter Number : "))
n=a;
sum=0;
while(a!=0):
    rem=a%10;
    fact=1;
    for i in range(1,rem+1) :
        fact=fact*i;
    sum=sum+fact;
    a=a//10;
if n==sum :
    print(n,"Number is Krishnamurti")    
else :
    print(n,"Number is Not Krishnamurti")
print("Sum of all the digit factorial is : ",sum)
