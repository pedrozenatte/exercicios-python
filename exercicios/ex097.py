# Referente a aula016

# Faça um programa que tenha uma função chamada escreve(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    print('-' * (len(msg) + 10))
    print(msg .center(len(msg) + 10))
    print('-' * (len(msg) + 10))


escreva('Pedro Guilherme de Barros Zenatte')