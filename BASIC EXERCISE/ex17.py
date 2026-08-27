#patern 1
print("-----parten 1-----")
a=int(input("Enter the number:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")

#patern 2
print("-----parten 2-----")
for i in range(1,a+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")
    
#patern 3
print("-----parten 3-----")
for i in range(a,0,-1):
    for j in range(i,a+1,+1):
        print(j,end=" ")
    print("\n")

#patern 4
print("-----parten 4-----")
for i in range(1,a+1):
    for j in range(i,a+1):
        print(j,end=" ")
    print("\n")

#patern 5
print("-----parten 5-----")
for i in range(1,a+1):
    for j in range(a,a-i,-1):
        print(j,end=" ")
    print("\n")

#patern 6
print("-----parten 6-----")
for i in range(1,a+1):
    for j in range(1,(a+2)-i):
        print(j,end=" ")
    print("\n")

#patern 7
print("-----parten 7-----")
for i in range(1,a+1):
    for j in range(a,i-1,-1):
        print(j,end=" ")
    print("\n")

#patern 8
print("-----parten 8-----")
for i in range(a,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")

#patern 9
print("-----parten 9-----")
k=1;
for i in range(1,a):
    for j in range(i,0,-1):
        print(k,end=" ")
        k=k+1;
    print("\n")

#patern 10
print("-----parten 10-----")
for i in range(1,a+1):
    for j in range(0,i):
        if j%2==0:
            print("1",end=" ")
        else:
             print("0",end=" ")
    print("\n")

#patern 11
print("-----parten 11-----")
k=1;
for i in range(1,a+1):
    for j in range(i,0,-1):
        b=k%2;
        print(b,end=" ")
        k=k+1;
    print("\n")

#patern 12
print("-----parten 12-----")
for i in range(1,a+1):
    print("   "*(a-i),end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")    
    print("\n")
    
#patern 13
print("-----parten 13-----")
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

#patern 14
print("-----parten 14-----")
for i in range(1,a+1):
    print("   "*(a-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

#patern 15
print("-----parten 15-----")
for i in range(1,a+1):
    print("   "*(a-i),end="")
    for j in range(i,0,-1):
        print("*",end=" ")
    for j in range(2,i+1):
        print("*",end=" ")    
    print("\n")

#patern ex
print("-----parten ex-----")
k=2;
for i in range(1,a+1):
    print("   "*(a-i),end="")
    for j in range(1,k):
        print("*",end=" ")
    k=k+2;
    print("\n")
