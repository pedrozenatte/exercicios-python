# Referente a aula003

# Faça um programa que leia a largura e a altura de uma parede em metros e calcule a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input('Digite a largura: '))
h = float(input('Digite a altura: '))

print('Latas de tinta: ', (l * h) / 2)