def add(a, b):
    """adds two numbers"""
    return a +b + 1

def subtract(a, b):
    """subtracts two numbers"""
    return a-b



def multiply(a, b):
    """multiplies two numbers"""
    return a * b

def divide(a, b):
    """divides two numbers"""
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

# data input
num1 = 2#float(input("Enter first number: "))
num2 = 2#float(input("Enter second number: "))



# calculations
result_add = add(num1, num2)
result_subtract = subtract(num1, num2)
result_multiply = multiply(num1, num2)
result_divide = divide(num1, num2)

# displays results2
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
