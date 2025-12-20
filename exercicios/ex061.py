# Referente a aula010

# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos usando a estrutura while.

a1 = float(input('Primeiro termo: '))
razao = float(input('Razão: '))
termos = 0

while termos < 10:
    print(a1 + (razao * termos))
    termos += 1 