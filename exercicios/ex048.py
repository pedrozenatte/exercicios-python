# Referente a aula009

# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0

for i in range(1, 500 + 1): 
    # Verificação de ímpar
    if i % 2 != 0:
        # Múltiplo de 3
        if i % 3 == 0:
            soma += i

print('Soma: {}' .format(soma))
