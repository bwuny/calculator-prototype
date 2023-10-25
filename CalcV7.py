def Addition(num1, num2): 
    return num1 + num2
def Subtraction(num1, num2): 
    return num1 - num2
def Multiplication(num1, num2): 
    return num1 * num2
def Division(num1, num2): 
    if num2 != 0: 
        return num1 / num2 
    else:
        return "the second number must be greater than 0."
def Percentage(num1, num2): 
    if num2 != 0: 
        return (num1 / 100) * num2
    else: 
        return "the second number must be greater than 0."
def Average(num1, num2, num3):
    return (num1 + num2 + num3) / 3
          
operations = [
    (1, Addition),
    (2, Subtraction),
    (3, Multiplication),
    (4, Division),
    (5, Percentage),
    (6, Average)]

for key, func in operations:
   print(f"{key}: {func.__name__}")

while True:    
    
    choice = float(input("choose an operation (1-6): "))
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))  
    
    if choice in operations:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '6':
            num3 = float(input("Enter the third number: "))
            Result = operations[choice](num1, num2, num3) 
        if choice == '5':
            print(f"Result: {Result}%")
    else:
        print("operation invalid. choose a valid operation (1-6).")
    another_calculation = str(input('another calculation? (yes ou no): ').lower())
    if another_calculation != 'yes':
        print('Bye!')
        break