# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = int(input('Digite o raio do círculo: '))
area = pow(raio,2) * math.pi
print(f'A área do círculo é: {round(area,1)}cm.')