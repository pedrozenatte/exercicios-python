# Referente a aula017

# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará.
# OBS: Use cores.


# Não usarei cores
def ajuda(): 
    print('=' * 31)
    print('SISTEMA DE AJUDA PyHELP' .center(31))
    print('=' * 31)

    while True:

        '''
        Um função iterativa para o help()
        
        :return: None
        :rtype: NoReturn
        '''

        func_biblio = str(input('Função ou Biblioteca > ')).strip().lower()

        if func_biblio == 'fim':
            break
        
        print('=' * (len(func_biblio) + 40))
        print(f'Acessando o manual do comando de {func_biblio}' .center(len(func_biblio) + 40))
        print('=' * (len(func_biblio) + 40))
        print()

        help(func_biblio)


ajuda() 