'''EX-9  Write a python program to enter a string, character to replace and replacement character. 
Output will be new string.
Input : Hello ! How are you ?
Character to replace : H
Replacement Character : P
Output : Pello ! Pow are you ?'''


string = input("Enter a string: ")
old = input("Character to replace: ")
new = input("Replacement character: ")

result = string.replace(old, new)

print("Output:", result)
