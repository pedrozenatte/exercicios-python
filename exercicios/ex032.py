# Referente a aula006

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 

import datetime

ano = int(input('Ano: '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Condição para ser bissexto
    print('{} é bissexto' .format(ano))
    
else: 
    print('{} não é bissexto' .format(ano))