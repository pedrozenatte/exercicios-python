# Referente a aula008

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal 
# De 25 até 30: Sobrepeso
# De 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)
print('IMC: {}' .format(imc))

if imc < 18.5:
    print('Abaixo do peso')

elif imc < 25:
    print('Peso ideal')

elif imc < 30:
    print('Sobrepeso')

elif imc < 40:
    print('Obesidade')

else:
    print('Obesidade mórbida')
