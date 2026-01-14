# Referente a aula016

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles e o maior. 

def maior(*valores: int):
    if valores == ():
        print('Foram informados 0 valores')
        return 0

    print(f'Foram informados {valores}')
    return max(valores)


print(f'Maior valor: {maior()}')