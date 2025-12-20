# Referente a aula010

# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. 

n_termos = int(input('N elementos: '))
termo = 0

antecessor1 = 1 
antecessor2 = 0
aux = 0

print('{} {}' .format(antecessor2, antecessor1), end = '')

while termo < n_termos:
    aux = antecessor2
    antecessor2 = antecessor1
    antecessor1 += aux

    print(' {}' .format(antecessor1), end = '')

    termo += 1

print('\n')



