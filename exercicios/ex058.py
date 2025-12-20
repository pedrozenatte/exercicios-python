# Referente a aula010

# Melhore o jogo do DESAFIO 028 em que o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. 

from random import randint

computador = randint(0, 10)
usuario = int(input('Qual valor o computador pensou: '))
contador = 0

while usuario != computador:
    print('ERRADO! Tente outra vez.')
    usuario = int(input('Qual valor o computador pensou: '))
    contador += 1

print('Acertou!\nTentativas necessárias:', contador)

# Tente deixar mais pythoniano 
# acertou = False
# palpites = 0

# while not acertou: # Aqui usamos o not ao invés de usuarop != computador
#     ...
