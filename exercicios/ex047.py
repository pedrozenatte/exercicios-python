# Referente a aula009

# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

contador = 0

for i in range(1, 51):
    # Então é par
    if i % 2 == 0: 
        contador += 1
        print('{} é Par' .format(i))

print('Entre 1 a 50 temos {} números pares' .format(contador))

# Podemos diminuir as iterações:
# for i in range(2, 51, 2):
#     print(n, end = '')
# print('Acabou!')

# Deixamos o programa mais rápido ocupando metade do tempo do processador