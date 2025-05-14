# Leia várias idades e calcule a média entre as idades (usar uma variável para idade).

idade = 0
media = 0
val = 10

for i in range(val):
    idade = int(input("Digite uma idade: "))
    media += idade

media /= val

print(f"A média das idades é de: {media}")