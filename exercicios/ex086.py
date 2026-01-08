# Referente a aula014

# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
# No fianl, mostre a matriz na tela com a formatação correta. 

matriz = [[None] * 3, 
          [None] * 3, 
          [None] * 3]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input('Valor: '))

print()
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