a = []

print("Enter 10 numbers:")

for i in range(10):
    n = int(input("Enter number: "))
    a.append(n)

# Sort numbers in ascending order
for i in range(10):
    for j in range(i + 1, 10):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

# Smallest 3
min1 = a[0]
min2 = a[1]
min3 = a[2]

# Largest 3
max1 = a[9]
max2 = a[8]
max3 = a[7]

print("min1 =", min1)
print("min2 =", min2)
print("min3 =", min3)

print("max1 =", max1)
print("max2 =", max2)
print("max3 =", max3)
