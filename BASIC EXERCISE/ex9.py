print("Enter 10 nombers.")
max=0
for i in range(1,11):
    num=int(input(print("Enter ",i," number")))
    sum=sum+num
    if num>max:
        max=num
print("maximum number is:",max)
