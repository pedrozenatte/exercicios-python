# Referente a aula006

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. 

salario = float(input('Salário: '))

if salario > 1250:
    print('Salário aumentado: {}' .format(salario * 1.1))

else: 
    print('Salário aumentado: {}' .format(salario * 1.15))