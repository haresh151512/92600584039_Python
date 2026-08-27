'''EX-10 Write a python program to count the digits in given string and also give sum of digits. If no digits 
available in string print 0.
Input : Hello123World
Output : No. of digits : 3
 Sum of digits : 6
Input : HelloWorld
Output : 0'''

s = input("Enter a string: ")
count = 0
sum = 0
for ch in s:
    if ch.isdigit():
        count = count + 1
        sum = sum + int(ch)
print("No. of digits:", count)
print("Sum of digits:", sum)
