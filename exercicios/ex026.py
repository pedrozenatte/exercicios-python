# Referente a aula005

# Faça um programa que leia uma frase pelo teclado e mostre: 
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece primeiro.
# Em que posição ela aparece a última vez. 

frase = str(input('Escreva uma frase: ')).strip() # Lembrando que se usar o strip direto, ele já remove espaços inúteis tanto da esquerda quanto da direita. 

print('A letra "A" aparece: {} vezes' .format(frase.lower().count('a')))
print('A primeira aparição começa na posição:', frase.lower().find('a') + 1)
print('A última aparição ocorre na posição: {}' .format(frase.lower().rfind('a') + 1))