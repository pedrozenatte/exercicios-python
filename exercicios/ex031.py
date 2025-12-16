# Referente a aula006

# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 paraviagens mais longas. 

distancia = float(input('Qual a distância da viagem: '))

if distancia <= 200:
    print('Passagem: {}' .format(0.5 * distancia))
else:
    print('Passagem: {}' .format(0.45 * distancia))