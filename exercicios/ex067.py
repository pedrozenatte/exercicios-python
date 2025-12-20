# Referente a aula011

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True:
    tabuada = int(input('Tabuada: '))

    if tabuada < 0:
        break

    for i in range(1, 11):
        print(f'{tabuada} x {i:2} = {tabuada * i}')
