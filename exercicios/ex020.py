# Referente a aula004

# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

import random

nome1 = input('Nome1: ')
nome2 = input('Nome2: ')
nome3 = input('Nome3: ')
nome4 = input('Nome4: ')

nomes = [nome1, nome2, nome3, nome4]

sorteados = random.sample(nomes, 4)

# Poderiamos utilizar a função random.shuffle(nomes), e printar a lista ao final, pois essa função apenas embaralha a lista.

print('Os sorteados estão na ordem: ', sorteados)