# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    print("Resultado da soma: ", num1 + num2)
elif operacao == "-":
    print("Resultado da subtração: ",abs(num1 - num2))
elif operacao == "*":
    print("Resultado da multiplicação: ", num1 * num2)
elif operacao == "/":
    print("Resultado da divisão: ", num1 / num2)
else:
    print("Operação inválida!")

