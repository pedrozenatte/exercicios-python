# Referente a aula017

# Crie uum programa que tenha a função leiaInt(), que vai funcionar de forma semenlhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 

def leiaInt(frase: str = ''):
    if frase != '':
        print(frase, end = '')
    
    while True:
        n = str(input()).strip()

        if n.isdigit():
             return int(n)

        print('ERRO! Digite um número inteiro válido.')
        print(frase, end = '')



n = leiaInt('Digite um número: ')

print(f'O valor lido é: {n}')

