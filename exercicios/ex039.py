# Referente a aula008

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 
# Se ele ainda vai se alistar ao serviço militar. 
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo 

import datetime

ano_nascimento = int(input('Informe o ano de nascimento: '))

idade = datetime.date.today().year - ano_nascimento

if idade < 18:
    print('Faltam {} anos para se alistar no exército' .format(18 - idade))

elif idade == 18:
    print('Está na hora de se alistar para o exército')

else: 
    print('Já passaram {} anos que deveria ter se alistado' .format(idade - 18))