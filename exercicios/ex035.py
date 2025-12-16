# Referente a aula006

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar triângulo')

else:
    print("Não é possível formar triângulo")