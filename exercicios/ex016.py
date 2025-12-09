# Referente a aula004

# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. 

import math as m

num_real = float(input('Número real: '))

print('O número {:.4f} tem a parte inteira {}' .format(num_real, m.trunc(num_real)))
