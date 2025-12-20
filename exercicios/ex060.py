# Referente a aula010

# Faça um programa que leia um número qualquer e mostre o seu fatorial.

numero = int(input('Informe o valor: '))
fatorial = numero

while numero > 1:
    fatorial *= (numero - 1)
    numero -= 1

print('Fatorial:', fatorial)

# Existe um método de fatorial em math 
# import math 
# f = math.factorial(numero)