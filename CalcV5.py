# Define as operações
def Adição(x, y): return x + y
def Subtração(x, y): return x - y
def Multiplicação(x, y): return x * y
def Divisão(x, y): return x / y if y != 0 else "Não pode ser dividido por zero"
def Porcentagem(x, y): return (x / y) * 100 if y != 0 else "Erro"
def Média(x, y, z): return (x + y + z) / 3
# Mostra as opções
menu = {1: "adição", 2: "Subtração", 3: "Multiplicação", 4: "Divisão", 5 :"Porcentagem", 6 :"média"}

# Solicita ao usuário que escolha uma opção
print ("Escolha uma operação:")
for chave, valor in menu.items():
    print (f"{chave}: {valor}")

escolha = input("Escolha (1/2/3/4/5/6): ")
num1, num2 = map(float, input("Digite dois números separados por espaço: ").split())

# Se for média, pedir três números
if escolha == '6':
    num3 = float(input("Número 3: "))
    resultado = Média(num1, num2, num3)
    print("resultado:", resultado)
elif escolha == '4':
    resultado = Divisão(num1, num2)
    print("resultado:",resultado)
    
elif escolha == '5':
    resultado = Porcentagem(num1, num2)
    print("resultado:",resultado, "%")
