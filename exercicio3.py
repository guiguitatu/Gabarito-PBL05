# Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

numero = int(input("Digite um numero: "))

for i in range(1, 11):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")