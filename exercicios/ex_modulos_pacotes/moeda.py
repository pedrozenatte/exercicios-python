# Módulo moeda

# Referente aos ex107 e ex108

def metade(preco: float):
    """
    Cálcula a metade do preço passado
    
    :param preco: Preço do produto
    :type preco: float
    :return: (float) preço pela metade
    """
    return preco / 2 

def dobro(preco: float):
    """
    Cálcula o dobro do preço passado
    
    :param preco: Preço do produto
    :type preco: float
    :return: (float) Dobro do preço
    """
    return preco * 2

def aumentar(preco: float, porcentagem: float):
    """
    Aumenta o preço em x porcento
    
    :param preço: Preço do produto
    :type preço: float
    :param porcentagem: Porcentagem de aumento (por exemplo: 10 representa 10%)
    :type porcentagem: float
    :return: (float) Preço aumentado
    """

    return preco * (1 + (porcentagem / 100))

def diminuir(preco: float, porcentagem: float):
    """
    Diminui o preço em x porcento
    
    :param preco: Preço do produto
    :type preco: float
    :param porcentagem: Porcentagem de diminuição (por exemplo: 10 representa 10%)
    :type porcentagem: float
    :return: (float) Preço diminuido
    """

    return preco * (1 - (porcentagem / 100))

def moeda(preco: float):
    """
    Formata em moeda o preço do produto
    
    :param preco: Preço do produto
    :type preco: float
    :return: str
    """

    frase = f'R${preco:.2f}'

    return frase