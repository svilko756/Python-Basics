num = int(input("Enter a num: "))

comp = "Greather than 10" if num > 10  else "Less than 10"

print(comp)

num = int(input("Enter a number: "))
condition = num % 2 == 0 
check = "Your number is even" if condition else "Your number is odd"

print(check)

num = int(input("Enter first number: "))
num_2 = int(input("Enter a second number: "))

condition = "Number 1 is greater than Number 2" if num > num_2 else "Number 2 is greater than Number "


print(condition)

weather = float(input("How is the weather in Ruse? "))

status = "The weather is good today" if weather > 19.5 and weather < 30 else "The weather is bad today"
print(status)