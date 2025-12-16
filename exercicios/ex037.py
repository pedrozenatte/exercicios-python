# Referente a aula008

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input('Informe o numero a ser transformado: '))

opcao = int(input('Selecione a opção de transformação\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))


if opcao == 1:
    transformacao = bin(numero)[2:]

elif opcao == 2:
    transformacao = oct(numero)[2:]

elif opcao == 3:
    transformacao = hex(numero)[2:]

else: 
    print('ERROR -1')
    exit()

print('Transformação: {}' .format(transformacao))