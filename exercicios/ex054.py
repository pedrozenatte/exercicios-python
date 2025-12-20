# Referente a aula009

# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores. 

import datetime

lista_ano = [0] * 7
contador = 0

for i in range(7):
    lista_ano[i] = int(input('Informe o ano de nascimento da pessoa {}: ' .format(i + 1)))
     # Transformando na idade
    lista_ano[i] = datetime.date.today().year - lista_ano[i] 
    if(lista_ano[i] < 21):
        contador += 1

print('{} pessoas não atingiram a maioridade e {} atingiram a maioridade' .format(contador, 7 - contador))
        
