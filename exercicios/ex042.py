# Referente a aula008

# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais.
# Isósceles: dois lados iguais. 
# Escaleno: todos os lados diferentes.

print('Informe os três lados do possível triângulo: ')
l1 = float(input())
l2 = float(input())
l3 = float(input())

# Verificando a existência de triângulo
if (l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2): # É possível formar triângulo
    
    if l1 == l2 and l1 == l3:
        print('Triângulo EQUILÁTERO')

    elif l1 == l2 or l1 == l3 or l2 == l3: 
        print('Triângulo ISÓSCELES')

    else: # Todos os lados diferentes
        print('Triângulo ESCALENO')

else:
    print('Não é possível formar triângulo')
