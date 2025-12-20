# Referente a aula010

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Sexo: ')).strip().upper()
print(sexo)

while sexo != 'M' and sexo != 'F':
    # Leia novamente
    print('Erro! Informe novamente.')
    sexo = str(input('Sexo: ')).strip().upper()

print('Sexo registrado com sucesso!')


# Outra forma
# while sexo not in 'MmFf':
    # Fazer igual
