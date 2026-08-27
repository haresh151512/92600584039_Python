print('a.')
for i in range(1,11):
    print(i,end=' ')
    
print('\n')

print('b.')
for i in range(2,21,2):
    print(i,end=' ')

print('\n')

print('c.')
for i in range(1,20,2):
    print(i,end=' ')

print('\n')

print('d.')
for i in range(100,89,-1):
    print(i,end=' ')

print('\n')

print('e.')
for i in range(200,179,-2):
    print(i,end=' ')

print('\n')

print('f.')
n=int(input('Enter value of n (in integer) : '))
if n<0:
    print('please enter non-negative integer : ')
elif n==0:
    pass;
elif n==1:
    print(0)
else:
    a,b=0,1;
    print(a,b,end=' ')
    for i in range(2,n):
        c=a+b;
        print(c,end=' ')
        a,b=b,c;
    
print('\n')

print('g.')
n=int(input('Enter the value of n (in integer) : '))
ans=0;
for i in range(1,n):
    print(i,' + ',end=' ')
    ans=ans+i;
print(n,end=' ')
ans=ans+n;
print('\nans=',ans)

print('\n')

print('h.')
n=int(input('Enter the value of n (in integer) : '))
ans=0;
for i in range(1,n):
    print(i,'/',i+1,' + ',end='')
    ans=ans+(i/(i+1));
print(n,'/',n+1,end='')
ans=ans+(n/(n+1));
print('\nans=',ans)

print('\n')

print('i.')
n=int(input('Enter the value of n (in integer) : '))
ans=0;
for i in range(1,n):
    print(i,'/',i*10,' + ',end='')
    ans=ans+(i/(i*10));
print(n,'/',n*10,end='')
ans=ans+(n/(n*10));
print('\nans=',ans)








    
