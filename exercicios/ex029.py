# Referente a aula006

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite. 

velocidade = int(input('Velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado!!! Valor da multa: {}' .format(7 * (velocidade - 80)))

else: 
    print('Nada ocorreu!!!')