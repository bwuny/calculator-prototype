     # Define as operações
while True:
    def Adição(x, y): return x + y
    def Subtração(x, y): return x - y
    def Multiplicação(x, y): return x * y
    def Divisão(x, y): return x / y 
    def Porcentagem(num1, num2): return (num1 / 100) * num2
    def Média(x, y, z): return (x + y + z) / 3
    
    # Mostra as opções
    menu = {1: "adição", 2: "Subtração", 3: "Multiplicação", 4: "Divisão", 5 :"Porcentagem", 6 :"Média"}
    
    # Solicita ao usuário que escolha uma opção
    print ("Escolha uma operação:")
    for chave, valor in menu.items():
        print (f"{chave}: {valor}")
        
    escolha = input("Escolha (1/2/3/4/5/6): ")
    num1 = float(input("Digite o primeiro número: ")) 
    num2 = float(input("Digite o segundo número: "))

    # Condições especiais
    if escolha == '6':
        num3 = float(input("Número 3: "))
        resultado = Média(num1, num2, num3)
        print("resultado:", resultado)
        
    if escolha == '4':
        if num2 != 0:
            resultado_divisão = Divisão(num1, num2)
            print("resultado:", resultado_divisão)
    else:
        print("Erro: Não pode ser dividido por zero")

       
    if escolha == '5':
        if num2 != 0:
            resultado_porcentagem = Porcentagem(num1, num2) 
            print("resultado:",resultado_porcentagem, "%")
    else:
        print("'o segundo número deve ser maior que zero'")
        
    outro_calculo = input('Outro cálculo? (sim ou não): ')
    if not outro_calculo.lower().startswith('s'):
        print('Até logo!')
        break