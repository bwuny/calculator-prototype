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

operations = [Addition,Subtraction,Multiplication,Division,Percentage,Average]
for key, func in enumerate(operations,start=1):
   print(f"{key}: {func.__name__}")

while True:    
    try:
        choice = int(input("choose an operation (1-6) "))
        if 1<= choice <= 6:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == 6:
                num3 = float(input("Enter the third number: "))
                Result = operations[choice-1](num1,num2,num3)
            else:
                Result = operations[choice-1](num1,num2)
            print(f"Result: {Result}")
        else:
            print("Operation invalid. Choose a valid operation (1-6).")
            if choice == 5:
                print(f"Result: {Result}%") # type: ignore
    except Exception as e:
        print("An error occurred:", e)   
    another_calculation = str(input('another calculation? (yes ou no): ').lower())
    if another_calculation == 'no':
        print('Bye!')
        break