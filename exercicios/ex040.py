# Referente a aula008

# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: APROVADO

p1 = float(input('Informe a nota da P1: '))
p2 = float(input('Informe a nota da P2: '))

media = (p1 + p2) / 2

if media < 5:
    print('Média {} --> \033[4;31;40mREPROVADO\033[m' .format(media))

elif media > 5 and media <= 6.9:
    print('Média {} --> \033[4;33;40mRecuperação\033[m' .format(media))

else: 
    print('Média {} --> \033[4;32;40mAPROVADO\033[m' .format(media))