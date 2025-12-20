# Referente a aula010

# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = int(input('Valor: '))

soma = n
contador = 1
maior = n
menor = n 
flag = 1

while flag == 1:
    continua = str(input('Deseja continuar (S/N): ')).lower().strip()
    
    while continua != 's' and continua != 'n': # while continua not in 'sn':
        print('Valor inválido!')
        continua = str(input('Deseja continuar (S/N): ')).lower().strip()

    if continua == 's': # while continua in 's'
        n = int(input('Valor: '))
        soma += n
        contador += 1

        if maior < n:
            maior = n
        if menor > n:
            menor = n
    
    else: 
        flag = 0

    
print('Média: {:.1f}\nMenor: {}\nMaior: {}' .format(soma / contador, menor, maior))