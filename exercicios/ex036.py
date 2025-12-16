# Referente a aula008

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
qnt_anos = int(input('Quantidade de anos para pagar a casa: '))

valor_prestacao = valor_casa / (qnt_anos * 12)

if valor_prestacao > 0.3 * salario: 
    print('Empréstimo NEGADO, valor da prestação supera o máximo aceito.')

else: 
    print('Empréstimo CONCEDIDO!')

print('Valor da prestação: {:.2f}' .format(valor_prestacao))
    
