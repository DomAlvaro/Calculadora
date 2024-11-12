def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."

def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")
    
    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {add(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtract(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiply(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {divide(num1, num2)}")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira números válidos.")
    else:
        print("Erro: Opção inválida. Por favor, selecione uma operação de 1 a 4.")

calculator()
