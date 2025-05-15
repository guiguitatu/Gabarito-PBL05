# .Dado um vetor A de tamanho N e um vetor B de tamanho N, crie um programa
# que calcule a soma dos elementos desses vetores e armazene o resultado em
# um vetor C de tamanho N. Regras:
# a. O tamanho dos vetores A, B e C é fornecido pelo usuário.
# b. Os elementos dos vetores A e B são fornecidos pelo usuário.
# c. A soma dos elementos de A[i] e B[i] deve ser armazenada em C[i].
# d. O vetor C deve ser exibido na tela após o cálculo.
# Exemplo de entrada/saída:
# Entrada:
# Tamanho dos vetores: 5
# Vetor A: 1 2 3 4 5
# Vetor B: 6 7 8 9 10
# Saída:
# Vetor C: 7 9 11 13 15

n = int(input("Digite o tamanho dos vetores: "))
a = [0] * n
b = [0] * n
c = [0] * n

for i in range(n):
    a[i] = int(input(f"Digite o elemento {i + 1} do vetor A: "))
    b[i] = int(input(f"Digite o elemento {i + 1} do vetor B: "))
    c[i] = a[i] + b[i]

print("Vetor A: ", a)
print("Vetor B: ", b)
print("Vetor C: ", c)

