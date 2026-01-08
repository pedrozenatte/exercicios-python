# Referente a aula014

# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
# dados_alunos = []
# notas = []

# Condição de parada '-'
while True: 
    nome = str(input('Nome: ')).strip()

    if nome == '-':
        break

    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

print('=' * 34)
print('BOLETIM' .center(34))
print('=' * 34)

print(f'{"ID":<4}{"Aluno":<20}{"Media":>10}')
for id, aluno in enumerate(alunos):
    print(f'{id + 1:<4}{aluno[0]:<20}{aluno[2]:>10}')

print('=' * 34)

while True:
    aluno = input('Mostrar notas de qual aluno: ')

    if aluno == '-':
        break
    
    aluno = int(aluno) - 1

    if int(aluno) >= len(alunos):
        print('Opção inválida... Tente outra vez!')

    else: 
        print(f'{"Aluno":<10}{"Nota 1":<10}{"Nota 2":<10}')
        print(f'{alunos[aluno][0]:<10}{alunos[aluno][1][0]:<10}{alunos[aluno][1][1]:<10}')

