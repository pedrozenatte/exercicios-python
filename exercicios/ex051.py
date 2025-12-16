# Referente a aula009

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

a1 = float(input('Informe o primeiro termo: '))
r = float(input('Informe a razão: '))

for i in range(10):
    print(a1 + (r * i))

# --- Outra forma ---

# a_novo = a1
# for i in range(10):
#     print(a_novo)
#     a_novo = a_novo + r