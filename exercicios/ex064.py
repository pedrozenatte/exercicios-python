# Referente a aula010

# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi asoma entre eles (desconsiderando o flag).

n = 0
contador = 0
soma = 0

while n != 999:
    n = int(input('Número: '))

    if n != 999:
        contador += 1
        soma += n

print('Quantidade de números: {}\nSomatória: {}' .format(contador, soma))