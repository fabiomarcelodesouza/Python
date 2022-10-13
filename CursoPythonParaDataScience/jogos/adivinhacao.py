def AdivinhacaoComWhile(tentativas):
    print('******************************')
    print('*    Jogo da adivinhação     *')
    print('******************************')
    
    numero_secreto = 42    

    while tentativas > 0:
        chute = int(input('Você possui {} tentativas. Digite seu palpite:\n'.format(tentativas)))
        print('Seu palpite é: {}'.format(chute))

        if chute == numero_secreto:
            print('VOCÊ ACERTOU, PARABÉNS!')
        elif chute > numero_secreto:
            print('VOCÊ ERROU, SEU PALITE FOI MAIOR QUE O NUMERO SECRETO, VOCÊ SE FODEU!')
        else:
            print('VOCÊ ERROU, SEU PALITE FOI MENOR QUE O NUMERO SECRETO, VOCÊ SE FODEU!')

        tentativas = tentativas - 1
        print('')

def AdivinhacaoComFor(tentativas):
    print('******************************')
    print('*    Jogo da adivinhação     *')
    print('******************************')

    numero_secreto = 42    

    for rodada in range(1, tentativas + 1):
        chute = int(input('Você possui {} tentativas. Digite seu palpite:\n'.format(tentativas + 1 - rodada)))
        print('Seu palpite é: {}'.format(chute))

        if chute == numero_secreto:
            print('VOCÊ ACERTOU, PARABÉNS!')
        elif chute > numero_secreto:
            print('VOCÊ ERROU, SEU PALITE FOI MAIOR QUE O NUMERO SECRETO, VOCÊ SE FODEU!')
        else:
            print('VOCÊ ERROU, SEU PALITE FOI MENOR QUE O NUMERO SECRETO, VOCÊ SE FODEU!')

        print('')