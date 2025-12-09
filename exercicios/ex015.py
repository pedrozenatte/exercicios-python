# Referente a aula003

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos KM foram rodados: '))

print('O valor a ser pago pelo aluguel é R${:.2f}' .format(dias * 60 + km * 0.15))