a=int(input('Enter values : '))
rev=0;
n=a;
while(n!=0):
    rem=n%10;
    rev=rev*10+rem;
    n=n//10
if a==rev:
    print(a , 'reverse is : ',rev)
    print('number is palindrom')
else:
    print(a , 'reverse is : ',rev)
    print('number is not palindrom')
