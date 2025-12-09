# Referente a aula004

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostr o comprimento da hipotenusa

import math

co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))

#hi = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))

hi = math.hypot(co, ca)

print('A hipotenusa é: {:.0f}' .format(hi))