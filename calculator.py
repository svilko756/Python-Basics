import math

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus (x, y):
    return x % y

def power(x,y):
    pow_number = math.pow(x, y)
    return pow_number

def main():
    a = input("Enter number for calculation: ")
    b = input("Enter number for calculation: ")
    
    while a == "" or b == "":
        print("Please do not leave it empty")
        a = input("Enter number for calculation: ")
        b = input("Enter number for calculation: ")
    
    num_a = int(a)
    num_b = int(b)

    operator = input("Choose operator to work (+, -, *, /, %, pow): ")

    if operator == "+" : 
        print(plus(num_a, num_b))
    elif operator == "-":
        print(minus(num_a, num_b))
    elif operator == "*":
        print(multiply(num_a, num_b))
    elif operator == "/":
        print(divide(num_a, num_b))
    elif operator == "%":
        print(modulus(num_a, num_b))
    elif operator == "pow":
        print(power(num_a, num_b))
    else:
        print("You cannot conttinie")

if __name__ == "__main__":
    main()