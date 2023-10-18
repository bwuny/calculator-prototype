def is_not_zero(num2):return num2 != 0     

     # Define as operações
def Adição(num1, num2): 
    return num1 + num2
def Subtração(num1, num2): 
    return num1 - num2
def Multiplicação(num1, num2): 
    return num1 * num2
def Divisão(num1, num2): 
    if is_not_zero(num2): 
        return num1 / num2 
    else:
        return "Divisão por zero não é permitida."
    
def Porcentagem(num1, num2): 
    if is_not_zero(num2): 
        return (num1 / 100) * num2
    else: 
        return "Porcentagem de zero não é permitida."
    
def Média(num1, num2, num3):
    return (num1 + num2 + num3) / 3

    escolha = input("Escolha a operação (1-6): ")        
   
   
operations = {
        '1': Adição,
        '2': Subtração,
        '3': Multiplicação,
        '4': Divisão,
        '5': Porcentagem,
        '6': Média}

while True:
    
    menu={1:"Adição", 2:"Subtração", 3:"Multiplicação",4:"Divisão",5:"Porcentagem", 6:"Média"}
    
    escolha = input("Escolha a operação (1-6): ")
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))  
    
    if escolha in operations:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if escolha == '6':
            num3 = float(input("Digite o terceiro número: "))
            resultado = operations[escolha](num1, num2) 
            
        if escolha != '6':
            operations[escolha](num1, num2, num3)
        if escolha == '5' and resultado != "Porcentagem de zero não é permitida":
            print(f"Resultado: {resultado}%")
        else:
            print(f"Resultado: {resultado}")
    else:
        print("Operação inválida. Escolha uma operação válida (1-6).")
    outro_calculo = input('Outro cálculo? (sim ou não): ').lower()
    if outro_calculo != 'sim':
        print('Até logo!')
        break

