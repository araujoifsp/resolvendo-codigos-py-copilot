# Agora vamos calcular a média de três notas fornecidas na entrada do usuário.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

print("A média das notas é: {:.2f}".format(media))