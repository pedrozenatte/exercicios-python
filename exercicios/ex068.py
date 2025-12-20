# Referente a aula011

# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

contador = 0
jogador = ''

while jogador not in ('par', 'ímpar', 'impar'):
    jogador = str(input('Escolha PAR/ÍMPAR: ')).strip().lower()

    if jogador not in ('par', 'ímpar', 'impar'):
        print('Opção inválida... Tente outra vez.')

while True:
    computador = randint(0, 9)
    valor = int(input('Valor: '))
    print(f'Computador: {computador} vs Jogador: {valor}')

    if jogador in 'par':
        if (valor + computador) % 2 == 0: # Jogador ganhou
            contador += 1
            print('Você ganhou a partida!!!')
        
        else:
            print('Você perdeu...')
            print(f'Partidas consecutivas ganhas: {contador}')
            print('Saindo...')
            sleep(3)
            break
    
    elif jogador in ('ímpar', 'impar'):
        if (valor + computador) % 2 == 0: # Jogador perdeu
            print('Você perdeu...')
            print(f'Partidas consecutivas ganhas: {contador}')
            print('Saindo...')
            sleep(3)
            break
        
        else:
            contador += 1
            print('Você ganhou a partida!!!')

