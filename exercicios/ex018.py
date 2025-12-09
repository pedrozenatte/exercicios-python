# Referente a aula004

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math as m

alfa = float(input('Valor do ângulo: '))

seno = m.sin(m.radians(alfa))
cos = m.cos(m.radians(alfa))
tan = m.tan(m.radians(alfa))

print('Seno : {:.2f}, Cosseno: {:.2f}, Tangente: {:.2f}' .format(seno, cos, tan))