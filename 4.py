# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

soma = 0
media = 0
contador = 1

while contador <= 4:
    nota = float(input(f'Digite a {contador}ª nota: '))
    soma+=nota
    contador+=1

media =  soma / (contador - 1)

print(f'A média bimestral foi de {media}.')