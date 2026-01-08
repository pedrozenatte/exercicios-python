# Referente a aula014

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta. 

from random import randint
from time import sleep

jogo = [None] * 6
tot_jogos = []
numero = None
contador = 0

qnt_jogos = int(input('Quantos jogos: '))


# for i in range(qnt_jogos):
#     for j in range(6):
#         numero = randint(1, 60)
        
#         if numero not in jogo:
#             jogo[j] = numero

#     tot_jogos.append(jogo[:])

# CUIDADO: Se fizer tot_jogos.append(jogo), voce estaria fazendo a mesma coisa que tot_jogos = jogo, e isso não seria uma cópia, isto é, você está reutilizando a MESMA lista jogo em todas as iterações e só adicionando a referência dela em tot_jogos. Ou seja: tot_jogos fica com várias referências para o mesmo objeto. Quando você muda jogo, todos mudam juntos, por isso tudo vira o último jogo.

# Utiizando o for existe a possibilidade de ter um none no meio (MUITO RARO, mas existe), pois se ele sortear o mesmo número duas vezes, e é a primeira vez que a lista está sendo preenchida, aquele número vai ser perdido e a iteração inteira é perdida, pois ocorre j++, além de que se não for a primeira vez, se o número sorteado já estiver na lista, aquele número não será substituído, o que pode diminuir a aleatoriedade.

for i in range(qnt_jogos):
    while contador < 6:
        numero = randint(1, 60)
        
        if numero not in jogo:
            jogo[contador] = numero
            contador += 1

    jogo.sort()
    tot_jogos.append(jogo[:])
    contador = 0

for i in range(qnt_jogos):
    print(f'Jogo {i + 1}: {tot_jogos[i]}')
    sleep(0.5)