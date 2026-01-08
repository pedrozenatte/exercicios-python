# Referente a aula014

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. 

numeros = []
contador = 0 # Marca a última posição - 1 do valor ímpar

for i in range(7):
    # Se for ímpar, insere na primeira posiçao, se for par na última
    numero = int(input('Valor: '))

    if numero % 2 == 0:
        numeros.append(numero)
    
    else: 
        numeros.insert(0, numero)
        contador += 1

numeros[:contador] = sorted(numeros[:contador])
numeros[contador:] = sorted(numeros[contador:])

print(f'Números: {numeros}')
print(f'Ímpares: {numeros[:contador]}\nPares: {numeros[contador:]}')

# Poderíamos ter feito com duas listas dentro da lista principal
# numeros = [[], []]

# Depois só colocar pares na 0 e ímpares na 1 e ordenar a lista com numeros[0].sort()
