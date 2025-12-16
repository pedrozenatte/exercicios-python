# Referente a aula005

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 

nome_completo = input('Nome completo: ')

lista_nome = nome_completo.split()

print('Primeiro nome: {}\nÚltimo nome: {}' .format(lista_nome[0], lista_nome[len(lista_nome) - 1]))