# Referente a aula009

# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. 

pesos = [0] * 5

for i in range(5):
    pesos[i] = float(input('Informe o peso {}: ' .format(i + 1)))

# maior = max(pesos)
# menor = min(pesos)

maior = pesos[i]
menor = pesos[i]

for i in range(5):
    if pesos[i] < menor:
        menor = pesos[i]
    if pesos[i] > maior:
        maior = pesos[i]

print('Peso menor: {}\nPeso maior: {}' .format(menor, maior))