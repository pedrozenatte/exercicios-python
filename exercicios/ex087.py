# Referente a aula014

# Aprimore o desafio anterios, mostrando no final: 
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha.

soma_par = 0
soma_col = 0
maior = 0

matriz = [[None] * 3,
          [None] * 3,
          [None] * 3]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input('Valor: '))

print('Matriz: ')
for i in range(3):
    for j in range(3):
        if j == 0:
            print('|', end = '')
        
        if j == 2:
            print(f'{matriz[i][j]:2}', end = '')
            print('|', end = '')
        
        else: 
            print(f'{matriz[i][j]:2} ', end = '')

    print()       

for m in matriz:
    for i in range(3):
        if m[i] % 2 == 0:
            soma_par += m[i]

# for m in matriz:
#     soma_col += m[2]

soma_col = sum(m[2] for m in matriz)

maior = max(matriz[1])

print(f'Soma dos pares: {soma_par}\nSoma da terceira coluna: {soma_col}\nMaior valor da segunda linha: {maior}')
