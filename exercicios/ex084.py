# Referente a aula014

# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# Uma listagem com as pessoas mais pesadas. 
# Uma listagem com as pessoas mais leves. 

pessoas = []
pessoas_pesadas = []
pessoas_leves = []

# Condição de parada: '-'
while True:
    # pessoas.append([str(input('Nome: ')).strip(), float(input('Peso: '))])
    nome = str(input('Nome: ')).strip()

    if nome == '-':
        break

    peso = float(input('Peso: '))

    pessoas.append([nome, peso])

# max_peso = pessoas[0][1]
# min_peso = pessoas[0][1]

# for i in range(len(pessoas)):
#     if max_peso < pessoas[i][1]:
#         max_peso = pessoas[i][1]
    
#     if min_peso > pessoas[i][1]:
#         min_peso = pessoas[i][1]

# OU

# for p in pessoas:
#     if max_peso < p[1]:
#         max_peso = p[1]
    
#     if min_peso > p[1]:
#         min_peso = p[1]

# Podemos substituir o encontro do máximo e do mínimo da seguinte maneira: 
max_peso = max(p[1] for p in pessoas)
min_peso = min(p[1] for p in pessoas)

for p in pessoas:
    if max_peso == p[1]:
        pessoas_pesadas.append(p[0])
    
    if min_peso == p[1]:
        pessoas_leves.append(p[0])


print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'Pessoas leves: {pessoas_leves}')
print(f'Pessoas pesadas: {pessoas_pesadas}')
