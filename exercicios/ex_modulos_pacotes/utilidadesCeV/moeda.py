# Módulo moeda

def metade(preco: float, formatacao: bool = False):
    """
    Cálcula a metade do preço passado
    
    :param preco: Preço do produto
    :type preco: float
    :param formatacao: Indica se o retorno vem no formato de moeda
    :type formatacao: bool
    :return: Se formatacao = False, (float) preço pela metade, senão str
    """

    if formatacao == True:
        frase = f'R${(preco / 2):.2f}'.replace('.', ',')

        return frase

    return preco / 2 

def dobro(preco: float, formatacao: bool = False):
    """
    Cálcula o dobro do preço passado
    
    :param preco: Preço do produto
    :type preco: float
    :param formatacao: Indica se o retorno vem no formato de moeda
    :type formatacao: bool
    :return: Se formatacao = False, (float) Dobro do preço, senão str
    """

    if formatacao == True:
        frase = f'R${(preco * 2):.2f}'.replace('.', ',')

        return frase

    return preco * 2

def aumentar(preco: float, porcentagem: float, formatacao: bool = False):
    """
    Aumenta o preço em x porcento
    
    :param preço: Preço do produto
    :type preço: float
    :param porcentagem: Porcentagem de aumento (por exemplo: 10 representa 10%)
    :type porcentagem: float
    :param formatacao: Indica se o retorno vem no formato de moeda
    :type formatacao: bool
    :return: Se formatacao = False, (float) Preço aumentado, senão str
    """

    if formatacao == True:
        frase = f'R${(preco * (1 + (porcentagem / 100))):.2f}'.replace('.', ',')

        return frase

    return preco * (1 + (porcentagem / 100))

def diminuir(preco: float, porcentagem: float, formatacao: bool = False):
    """
    Diminui o preço em x porcento
    
    :param preco: Preço do produto
    :type preco: float
    :param porcentagem: Porcentagem de diminuição (por exemplo: 10 representa 10%)
    :type porcentagem: float
    :param formatacao: Indica se o retorno vem no formato de moeda
    :type formatacao: bool
    :return: Se formatacao = False, (float) Preço diminuido, senão str
    """

    if formatacao == True:
        frase = f'R${(preco * (1 - (porcentagem / 100))):.2f}'.replace('.', ',')

        return frase

    return preco * (1 - (porcentagem / 100))

def moeda(preco: float):
    """
    Formata em moeda o preço do produto
    
    :param preco: Preço do produto
    :type preco: float
    :return: str
    """

    frase = f'R${preco:.2f}'.replace('.', ',')

    return frase

def resumo(preco: float, porcent_aumento: float = 0, porcent_reduc: float = 0):
    """
    Apresenta o resumo do preço
    
    :param preco: Preço do produto
    :type preco: float
    :param porcent_aumento: Porcentagem de aumento em (%)
    :type porcent_aumento: float
    :param porcent_reduc: Porcentagem de diminuição em (%)
    :type porcent_reduc: float
    :return: str 
    """

    print('-' * 30)
    print('RESUMO DO VALOR' .center(30))
    print('-' * 30)

    print(f'{"Preço analisado:":<21}{moeda(preco):<10}')
    print(f'{"Dobro do preço:":<21}{dobro(preco, True):<10}')
    print(f'{"Metade do preço:":<21}{metade(preco, True):<10}')
    print(f'{porcent_aumento}% {"de aumento:":<17}{aumentar(preco, porcent_aumento, True):<10}')
    print(f'{porcent_reduc}% {"de redução:":<17}{diminuir(preco, porcent_reduc, True):<10}')

