def transform():
    text = str(input('Texto a ser transformado: '))
    while True:
        type = str(input('Tipo da transformação (uppercase, lowercase, capitalize, removemultiplespaces, removespaces): '))

        if (type == 'uppercase'):
            text = text.upper()
            break
        elif (type == 'lowercase'):
            text = text.lower()
            break
        elif (type == 'capitalize'):
            array = text.split(' ')
            text = ''
            for i in array: text += f'{i.capitalize()} '
            break
        elif (type == 'removemultiplespaces'):
            array = text.split(' ')
            text = ''
            array = filter(lambda x: x != '', array)
            for i in array: text += f'{i.strip()} '
            break
        elif (type == 'removespaces'):
            array = text.split(' ')
            text = ''
            array = filter(lambda x: x != '', array)
            for i in array: text += i.strip()
            break
        else:
            print('\n\nDigite o tipo corretamente.\n')    
    
    print('\n\n')
    print(text)

    close_program = str(input('Fechar programa? (Y/N) '))

    if close_program.lower() == 'n': transform()

transform()