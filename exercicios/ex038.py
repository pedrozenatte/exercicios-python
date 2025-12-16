# Referente a aula008

# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = input('Informe o número 1: ')
n2 = input('Informe o número 2: ')

if n1 > n2:
    print('o Primeiro valor {} é maior' .format(n1))

elif n2 > n1:
    print('O Segundo valor {} é maior' .format(n2))

else: 
    print('Não existe valor maior')