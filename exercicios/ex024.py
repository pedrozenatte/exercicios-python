# Referente a aula005

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input('Nome da cidade: ')
comparacao = 'Santo'

lista_nome = cidade.split()

print('Começa ou não com o nome SANTO: {}' .format(comparacao.upper() == lista_nome[0].upper()))

# --- Solução 2 ----
# cidade = str(input('Em que cidade você nasceu? ')).strip
# print(cidade[:5].upper() == 'SANTO')