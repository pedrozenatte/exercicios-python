# Referente a aula018

# Adpte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado. 

import moeda

p = float(input('Preço: '))
print(f'Metade de {moeda.moeda(p)}: {moeda.moeda(moeda.metade(p))}')
print(f'Dobro de {moeda.moeda(p)}: {moeda.moeda(moeda.dobro(p))}')
print(f'Aumento de 10%: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuir 13%: {moeda.moeda(moeda.diminuir(p, 13))}')