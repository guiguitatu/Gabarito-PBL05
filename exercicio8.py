#Faça um algoritmo que leia 10 números inteiros, armazene-os em um vetor e
# imprima em ordem crescente.

vet = [0] * 10

for i in range(10):
    vet[i] = int(input("Digite um número inteiro: "))

for i in range(10):
    for j in range(i + 1, 10):
        if vet[i] > vet[j]:
            vet[i], vet[j] = vet[j], vet[i]

print("Os números em ordem crescente são:")
for i in range(10):
    print(vet[i])
