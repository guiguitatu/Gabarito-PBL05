# Utilizando a estrutura de repetição for, faça um programa que receba 10
# números e conte quantos deles estão no intervalo [10,20] e quantos deles
# estão fora do intervalo.

num = 0 
dentro = 0
fora = 0

for i in range (10):
    num = int(input("Digite um número: "))

    if 20 >= num >= 10:
        dentro += 1
    else: 
        fora += 1
    
print(f"Foi digitado {dentro} numeros dentro do intervalo e {fora} numeros fora do intervalo.")
