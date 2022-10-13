def verifica_se_pode_dirigir(idade):
    if idade >= 18:
        print('Sua idade é {} anos, parabéns, você pode dirigir e fazer outras merdas.'.format(idade))
    else:
        print('Sua idade é {} anos, você é um crianção e não pode dirigir.'.format(idade))

idade = int(input('Informe sua idade:\n'))
verifica_se_pode_dirigir(idade)