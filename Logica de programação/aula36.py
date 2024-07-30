while True:
    print('Numero')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    # lower() #muda de maiuculo para minusculo
    # startswith('s') #começo de cada linha 

    if sair is True:
        break