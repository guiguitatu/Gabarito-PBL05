# Ler 10 números e imprimir quantos são pares e quantos são ímpares.

pares = 0
impares = 0
num = 0

for i in range (10):
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares +=1
print(f"Foi digitados {pares} numeros pares e {impares} numeros inpares.")