# Referente a aula011

# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

contador = 0
soma = 0

while True:
    n = int(input('Valor (999 para parar): '))

    if n == 999:
        break

    contador += 1
    soma += n

print(f'Número digitados: {contador}\nSoma: {soma}')