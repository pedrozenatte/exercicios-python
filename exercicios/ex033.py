# Referente a aula006

# Faça um programa que leia três número e mostre qual é o maior e qual é o menor.

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))

# Forma lógica: 

maior = n1 
menor = n1

if n2 > maior: 
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('Maior: {}\nMenor: {}' .format(maior, menor))

# Forma python:

# maior = max(n1, n2, n3)
# menor = min(n1, n2, n3)
