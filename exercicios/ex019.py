# Referente a aula004

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

nome1 = input('Nome1: ')
nome2 = input('Nome2: ')
nome3 = input('Nome3: ')
nome4 = input('Nome4: ')

nomes = [nome1, nome2, nome3, nome4]

sorteado = random.choice(nomes)
# OBS: choice devolve uma string, choices devolve uma lista com uma string

print('O sorteado foi: ', sorteado)
