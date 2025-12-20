# Referente a aula009

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Informe a frase: ')
frase = frase.lower().split()
frase = ''.join(frase) 

palindromo = [''] * len(frase)

contador = len(frase)

for i in range(len(frase)):
    palindromo[i] = frase[contador - 1]
    contador -= 1

palindromo = ''.join(palindromo).lower()

# OBS: Da linha 9 até a linha 17, podemos substituir por: palindromo = frase[::-1].lower()
# Esse modelo é mais "pythoniano"

if(palindromo == frase):
    print('{} é palíndromo' .format(frase))

else:
    print('{} não é palíndromo' .format(frase))