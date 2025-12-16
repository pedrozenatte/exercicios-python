# Referente a aula005

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas. 
# Quantas letras ao todo (sem considerar os espaços).
# Quantas letras tem o primeiro nome. 

nome_completo = input('Informe o nome completo: ')
palavras_nome = nome_completo.split() # É uma lista
nome = ''.join(palavras_nome)

print(nome)
print('Nome em maiúsculo: ', nome_completo.upper())
print('Nome em minúsculo: ', nome_completo.lower())
print('Total de letras sem espaço:', len(nome))
print('Total de letras do primeiro nome: {}' .format(len(palavras_nome[0])))

# Voce pode cortar os espaços direto:
# nome = str(input('Informe o nome completo: ')).strip() # mas isso só tira espaços de antes de começar a string e depois de terminar
# print('Seu nome tem ao todo {} letras' . format(len(nome) - nome.count(' '))) # Vejo o total de letras e tiro da quantidade de espaços que a string possui
# print('Seu primeiro nome tem {} letras' .format(nome.find(' '))) # Aqui estamos procurando o primeiro espaço, que vai retornar a posição dele, que é exatamente a quantidade de letras do primeiro nome.