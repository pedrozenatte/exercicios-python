# Referente a aula017

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente. 

def ficha(nome: str = '<desconhecido>', gols: int = 0):
    '''
    Função que mostra a ficha de um jogador

    :param nome: Nome do jogador
    :type nome: str
    :param gols: Qnt de gols do jogador
    :type gols: int
    '''
    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Qnt de gols: ')).strip()

if nome == '' and gols == '':
    ficha()

elif nome == '':
    ficha(gols = int(gols))

elif gols == '':
    ficha(nome = nome)

else: 
    ficha(nome, int(gols))

