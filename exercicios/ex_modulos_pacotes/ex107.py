# Referente a aula018

# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()
# Faça também um programa que importe esse módulo e use algumas dessas funções. 

import moeda

p = float(input('Preço: '))
print(f'Metade de {p}: {moeda.metade(p)}')
print(f'Dobro de {p}: {moeda.dobro(p)}')
print(f'Aumento de 10%: {moeda.aumentar(p, 10)}')
print(f'Diminuir 13%: {moeda.diminuir(p, 13)}')
