# Referente a aula016

# Faça um programa que tenha uma função chamada cotnador(), que recebe três parâmtros: início, fim e passo e realiza a contagem. 
# Seu programa tem querealizar três contagens através da função criada: 
# De 1 até 10, de 1 em 1
# De 10 até 0, de 2 em 2
# Uma contagem personalizada. 

from time import sleep

def contador(inicio: int, fim: int, passo: int):
    if passo == 0:
        passo = 1

    if inicio < fim: 
        for i in range(inicio, fim + 1, passo):
            print(i)
            sleep(0.5)
    
    else: 
        if passo < 0:
            passo *= -1

        for i in range(inicio, fim - 1, -passo):
            print(i)
            sleep(0.5)


contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))