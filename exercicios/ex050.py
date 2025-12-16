# Referente a aula009

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

numeros = [0] * 6
soma = 0

for i in range(6):
    numeros[i] = int(input('Número {}: ' .format(i + 1)))

for i in range(6):
    # Verificação de par
    if numeros[i] % 2 == 0: 
        soma += numeros[i]

print('Soma: {}' .format(soma))