# Dado um vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete
# mais vezes.

vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

num = vetor[0]
contagem = 0

for i in range(len(vetor)):
    contagem_atual = 0
    for j in range(len(vetor)):
        if vetor[i] == vetor[j]:
            contagem_atual += 1

    if contagem_atual > contagem:
        contagem = contagem_atual
        num = vetor[i]

print(f"O número que mais se repete é: {num} (repetido {contagem} vezes)")
