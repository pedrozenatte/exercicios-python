# Referente a aula005

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. 

# numero = input('Digite um número de 0 a 9999: ')

# print('Unidade: {}' .format(numero[3]))
# print('Dezena: {}' .format(numero[2]))
# print('Centena: {}' .format(numero[1]))
# print('Unidade de milhar: {}' .format(numero[0]))

# A solução acima é problemática para valores que não possuem quatro dígitos

numero = int(input('Digite um número de 0 a 9999: '))

print('Unidade: {}' .format(numero % 10))
print('Dezena: {}' .format((numero // 10) % 10))
print('Centena: {}' .format((numero // 100) % 10))
print('Unidade de milhar: {}' .format((numero // 1000) % 10))

# O resto da divisão escolhe quantos números pegar, por exemplo, resto da divisão por 10 pega um número