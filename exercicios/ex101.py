# Referente a aula017

# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições. 

import datetime

def voto(ano_nascimento: int):
    
    '''
    Essa função calcula se uma pessoa tem voto negado, opcional ou obrigatório nas eleições. 
    
    :param ano_nascimento: Ano de nascimento da pessoa
    :type ano_nascimento: int
    :retorn: Retorna uma frase (str) dizendo opcional, obrigatório ou negado.
    '''

    idade = datetime.date.today().year - ano_nascimento

    if idade >= 18 and idade < 65:
        return 'obrigatório', idade
    
    elif idade < 18 and idade >= 16 or idade >= 65:
        return 'opcional', idade
    
    else:
        return 'negado', idade
    


resp = voto(int(input('Ano de nascimento: ')))
print(f'Com {resp[1]} anos o voto é {resp[0]}')