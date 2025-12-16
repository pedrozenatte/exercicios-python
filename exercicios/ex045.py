# Referente a aula008

# Crie um programa que faça o computador jogar jokenpô com você

import random
import time

print('Selecione a opção a ser jogada: ')
opcao = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\n'))

computador = random.randint(1, 3)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO...')

print('=' * 30)
if opcao == 1: # Pedra
    if computador == 1: # Pedra
        print('Empate!!!')

    elif computador == 2: # Papel
        print('Escolhi papel, GANHEI!!!')

    else: # Tesoura
        print('Escolhi tesoura, perdi...')

elif opcao == 2: # Papel
    if computador == 1: # Pedra
        print('Escolhi pedra, perdi...')

    elif computador == 2: # Papel
        print('Empate!!!')

    else: # Tesoura
        print('Escolhi tesoura, GANHEI!!!')

elif opcao == 3: # Tesoura
    if computador == 1: # Pedra
        print('Escolhi pedra, GANHEI!!!')

    elif computador == 2: # Papel
        print('Escolhi papel, perdi...')

    else: # Tesoura
        print('Empate')

else: 
    print('Opção inválida!')
print('=' * 50)



# --- OUTRA FORMA DE FZ --- #

# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = random.randint(0, 2)
# print('''Suas opções:
#       [ 0 ] PEDRA
#       [ 1 ] PAPEL
#       [ 2 ] TESOURA''')

# jogador = int(input('Qual é a sua jogada? '))

# print('-=' * 10)
# print('Computador jogou {}' .format(itens[computador]))
# print('Jogador jogou {}' .format(itens[jogador]))
# print('-=' * 10)

# O resto é igual praticamente 
