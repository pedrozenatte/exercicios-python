# Referente a aula011

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# Qual é o total gasto na compra. 
# Quantos produtos custam mais de R$1000,00
# Qual é o nome do produto mais barato.

tot_gasto = 0
contador = 0
primeira_repeticao = 0

while True:
    nome_produto = str(input('Nome do produto: ')).strip().lower()

    while True:
        preco = float(input('Preço do produto: '))

        if preco < 0:
            print('Valor inválido... Tente outra vez.')
        
        else: 
            break
    
    # Acumula o total gasto
    tot_gasto += preco

    # Conta valores acima de 1000
    if preco > 1000:
        contador += 1
    
    # Encontra menor valor
    if primeira_repeticao == 0:
        menor = preco
        nome_barato = nome_produto
        primeira_repeticao += 1

    elif menor > preco:
        menor = preco
        nome_barato = nome_produto
    #----------------------

    while True:
        continuar = str(input('Deseja continuar (S/N): ')).strip().lower()

        if continuar not in ('s', 'n'):
            print('Valor inválido... Tente outra vez.')

        else: 
            break

    if continuar == 'n': 
        break

print(f'Total gasto: {tot_gasto}\nQnt de produtos que custam mais de R$1000: {contador}\nNome do produto mais barato: {nome_barato}')