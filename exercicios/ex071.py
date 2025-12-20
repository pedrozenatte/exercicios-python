# Referente a aula011

# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1 = 0

while True:
    saque = int(input('Valor a ser sacado: '))

    if saque < 0:
        print('Valor inválido... Tente outra vez.')
    
    else: 
        break

if saque > 0:
    if (saque // 50) > 0:
        cedula50 = saque // 50
        saque -= (50 * cedula50)
    
    if (saque // 20) > 0:
        print(saque // 20)
        cedula20 = saque // 20
        saque -= (20 * cedula20)

    if (saque // 10) > 0:
        print(saque // 10)
        cedula10 = saque // 10
        saque -= (10 * cedula10)

    if saque > 0:
        cedula1 = saque
        saque -= cedula1
        
print('Saque:',saque)
print(f'Notas de 50: {cedula50}\nNotas de 20: {cedula20}\nNotas de 10: {cedula10}\nMoedas de 1: {cedula1}')

