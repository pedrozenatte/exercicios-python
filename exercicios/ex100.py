# Referente a aula016

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior. 

from random import randint

def sorteia():
    lista = []
    contador = 0

    while contador < 5:
        numero = randint(1, 100)

        if numero not in lista:
            lista.append(numero)
            contador += 1
        
    return lista 


def somaPar(lista: list): 
    return sum(valor for valor in lista if valor % 2 == 0)

sorteados = sorteia()
print(sorteados)
print(somaPar(sorteados))


