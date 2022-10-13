def jogar():
    print('******************************')
    print('*    Jogo da forca           *')
    print('******************************')
    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    acertou = False
    acertos = 0
    tentativas = 7

    print(letras_acertadas)

    while(tentativas > 0 and acertos != len(palavra_secreta)):
        print('Você tem {} tentativas.'.format(tentativas))

        chute = input('Chute uma letra:\n').lower()
        posicao = 0

        for letra in palavra_secreta:
            if chute == letra:
                acertou = True
                acertos += 1
                letras_acertadas[posicao] = letra

            posicao  = posicao + 1    

        if acertou == True:
            acertou = False
        else:
            tentativas -= 1

        print(letras_acertadas)

    print('Fim do jogo!')