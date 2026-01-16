# Referente a aula017

# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

def notas(*notas : float, sit: bool = False): 

    '''
    Função que verifica a quantidade de notas, a maior nota, a menor nota, a média da turma e a situação da turma (ruim, média ou boa)
    
    :param notas: Uma tupla de várias notas
    :type notas: float
    :return: Um dicionário com as informações
    '''

    qnt_notas = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / qnt_notas
    
    if sit == True:
        if media < 5:
            situacao = 'Ruim'
        
        elif media >= 5 and media < 7:
            situacao = "Razoável"
        
        else: 
            situacao = 'Boa'

        return {'Quantidade de notas': qnt_notas, 'Maior nota': maior, 'Menor nota': menor, 'Media': media, 'Situacao': situacao}

    else:
        return {'Quantidade de notas': qnt_notas, 'Maior nota': maior, 'Menor nota': menor, 'Media': media}


notas_turma = notas(4, 5, 6.5, 10, 10, 10, 9, 10, sit = True)
print(notas_turma)
