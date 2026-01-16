# Referente a aula017

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor booleano (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial. 

def fatorial(valor: int, show: bool = False):

    '''
    Essa função calcula o fatorial de um número. 
    
    :param valor: Valor do fatorial a ser calculado
    :type valor: int
    :param show: Indica se quer ou não que mostre o processo de cálculo do fatorial
    :type show: bool
    :retorno: Retorna uma str se show = True, senão retorna apenas um inteiro
    '''
    
    repeticao = valor
    frase = []

    for i in range(valor - 1, 1, -1):
        valor *= i

    if show == True:
        for i in range(repeticao, 0, -1):
            if i == 1: # Última repetição
                # print(f'{i} = {valor}')
                frase.append(f'{i} = valor') 
            
            else: 
                # print(f'{i} x ', end = '')
                frase.append(f'{i} x ')

        frase = ''.join(frase)
        
        return frase
    
    else:
        return valor

print(fatorial(5, True))
fatorial()


