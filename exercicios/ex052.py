# Referente a aula009

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

numero = int(input('Informe o valor a ser analisado: '))

# 0 e 1 não é primo (muito menos negativos)
if numero < 2:
    print('{} não é primo' .format(numero))

# 2 e 3 são primos
elif numero == 2 or numero == 3: 
    print('{} é primo' .format(numero))

# Pares não são primos
elif numero % 2 == 0: 
    print('{} não é primo' .format(numero))

# Se for impar, é possível que seja primo
else: 
    for i in range(2, numero):
        if(numero % i) == 0:
            print('{} não é primo' .format(numero))
            exit()
        
    print('{} é primo' .format(numero))


