# Referente a aula009

# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. 

tabuada = int(input('Informa a tabuada: '))

print('Tabuada: ')
for i in range(10 + 1):
    print('{} x {:2} = {}' .format(tabuada, i, tabuada * i))

