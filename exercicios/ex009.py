# Referente a aula003

# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. 

a = int(input('Digite um valor: '))

print('Tabuada: ')
for i in range(11): 
    print('{} x {:2} = {}' .format(a, i, a * i))