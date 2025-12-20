# Referente a aula011

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados. 
# Quantas mulheres tem menos de 20 anos. 

contador_idade = 0
contador_homens = 0
cont_f_menos_20 = 0

while True:
    # Garantindo funcionalidade
    while True:
        idade = int(input('Idade: '))

        if idade < 0:
            print('Valor de idade inválido... Tente outra vez.')
        
        else:
            break
    
    while True:
        sexo = str(input('Sexo (M/F): ')).strip().lower()[0]

        if sexo not in ('m', 'f'): 
            print('Valor de sexo inválido... Tente outra vez.')
        
        else: 
            break

    # Fazendo os cálculos
    if idade > 18:
        contador_idade += 1

    if sexo == 'm': 
        contador_homens += 1
    
    if sexo == 'f' and idade < 20:
        cont_f_menos_20 += 1
    
    # Verificando se usuário quer continuar
    while True:
        continuar = str(input('Deseja continuar (S/N): ')).strip().lower()

        if continuar not in ('s', 'n'):
            print('Valor inválido... Tente outra vez')
        
        else: 
            break
    
    
    if continuar == 'n':
        break


print(f'Pessoas com mais de 18 anos: {contador_idade}\nHomens cadastrados: {contador_homens}\nMulheres com menos de 20 anos: {cont_f_menos_20}')

    
