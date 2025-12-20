# Referente a aula010

# Crie um programa que leia dois valores e mostre um menu na tela: 
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. 

valores = []

for i in range(2):
    valores.append(int(input('Informe o valor {}: ' .format(i + 1))))

print('''Selecione a opção:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
opcao = int(input('Opção: '))

while opcao == 4 or opcao < 1 or opcao > 5:
    if opcao == 4: # Selecionar dois novos valores
        valores.clear()

        for i in range(2):
            valores.append(int(input('Informe o valor {}: ' .format(i + 1))))

        print('''Selecione a opção:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
        opcao = int(input('Opção: ')) 

        
    
    else: # Opção inválida
        print('Opção inválida! Selecione outra.')
        opcao = int(input('Opção: '))
        

if opcao == 1:
    soma = valores[0] + valores[1]
    print('Soma:', soma)

elif opcao == 2: 
    mult = valores[0] * valores[1]
    print('Multiplicação:', mult)

elif opcao == 3:
    maior = max(valores)
    print('Maior:', maior)

else:
    print('Saindo...')
    exit()


