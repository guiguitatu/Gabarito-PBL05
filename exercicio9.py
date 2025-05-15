# Faça um algoritmo que solicita ao usuário um texto qualquer. Calcule quantas
# vogais existem no texto. Imprima quais vogais existem no texto e quantas são.

vogais = 0
vogais_str = ['a', 'e', 'i', 'o', 'u']
vogais_existentes = []

texto = input("Digite um texto: ").lower()

for letra in texto:
    if letra in vogais_str:
        vogais += 1
        if letra not in vogais_existentes:
            vogais_existentes.append(letra)
        
print("O texto contém", vogais, "vogais.")
print("As vogais existentes no texto são: ")
print(vogais_existentes)