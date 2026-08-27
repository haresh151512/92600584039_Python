a = []

print("Enter 10 numbers:")

for i in range(10):
    n = int(input("Enter number: "))
    a.append(n)

# Sorting in ascending order
for i in range(10):
    for j in range(i + 1, 10):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("Numbers in ascending order:")

for i in range(10):
    print(a[i], end=" ")
  
