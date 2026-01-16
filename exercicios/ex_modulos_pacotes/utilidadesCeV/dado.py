# Módulo dado

def leiaDinheiro(frase: str = ''): 
    while True: 
        print(f'{frase}', end = '')
        numero = str(input()).strip()
        
        if numero.count(',') == 1 or numero.count('.') == 1:
            numero = numero.replace(',', '.').split('.')

            if numero[0].isnumeric() and numero[1].isnumeric(): 
                numero = '.'.join(numero)
                numero = float(numero)
                break
        
        elif numero.count(',') == 0 or numero.count('.') == 0:
            if numero.isnumeric():
                numero = float(numero)
                break

        print('Valor inválido...Tente outra vez!')
        
    return numero