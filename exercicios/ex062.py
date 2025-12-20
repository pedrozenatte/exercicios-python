# Referente a aula010 

# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos. 

acumulado = float(input('Primeiro termo: '))
razao = float(input('Razão: '))

termos = 0
quantidade_termos = 9

print(acumulado)

while termos < quantidade_termos:
    acumulado += razao
    print(acumulado)
    termos += 1

    if termos == quantidade_termos:
        quantidade_termos = int(input('Deseja mostrar quantos termos a mais: '))
        termos = 0

        if quantidade_termos <= 0:
            exit()