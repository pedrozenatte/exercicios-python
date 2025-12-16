# Referente a aula006

# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
import time 

numero = random.randint(0, 5) 

print('PROCESSANDO...')
time.sleep(3)

num_usuario = int(input('Qual o valor que o computador "pensou"? '))

print('Acertou!' if numero == num_usuario else 'Errou!, valor pensado {}' .format(numero))