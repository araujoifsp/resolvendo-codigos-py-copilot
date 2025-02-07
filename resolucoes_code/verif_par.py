#  Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

num = int(input("Digite um número inteiro: "))
if num % 2 == 0: # Utilizando o operador de resto para verificar se é par
    print("O número é par.")
else:
    print("O número é ímpar.")
    