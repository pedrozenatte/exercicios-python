# Referente a aula018

# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# Foi criado um modulo chamado moeda2.py para modificar o moeda.py (para não perder o que foi feito nos ex 107 e 108)

import moeda2

p = float(input('Preço: '))
print(f'Metade de {p}: {moeda2.metade(p, True)}')
print(f'Dobro de {p}: {moeda2.dobro(p, True)}')
print(f'Aumento de 10%: {moeda2.aumentar(p, 10, True)}')
print(f'Diminuir 13%: {moeda2.diminuir(p, 13, True)}')