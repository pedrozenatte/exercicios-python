# Referente a aula016

# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura: float, comprimento: float): 
    return largura * comprimento


a = float(input('Largura: '))
b = float(input('Comprimento: '))

print(f'Área do terreno: {area(a, b)}m²')