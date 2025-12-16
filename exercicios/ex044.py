# Referente a aula008

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
# À vista dinheiro/PIX: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:=^50}' .format(' Lojas Zenatte'))
p_produto = float(input('Informe o preço do produto: '))
opcao = int(input('Forma de pagamento:\n1 - À vista no dinheiro/PIX\n2 - À vista no cartão\n3 - Dividir em 2x\n4 - Dividir em 3x ou mais\n'))

if opcao == 1: 
    print('Preço a ser pago: R${:.2f}' .format(p_produto * 0.9))

elif opcao == 2:
    print('Preço a ser pago: R${:.2f}' .format(p_produto * 0.95))

elif opcao == 3:
    print('Preço a ser pago: 2x de R${:.2f}' .format(p_produto / 2))

elif opcao == 4:
    parcelas = int(input('Informe em quantas vezes será parcelado: '))

    if parcelas < 3:
        print('Selecione a opção 3')
    else: 
        print('Preço a ser pago: R${:.2f}' .format((p_produto * 1.2) / parcelas))

else: 
    print('Opção inválida')

print('=' * 50)
    