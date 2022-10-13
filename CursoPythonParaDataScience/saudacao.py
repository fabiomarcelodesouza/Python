import py_compile

#Criando a função
def saudacao():
    nome = input('Qual seu primeiro nome?\n')
    sobrenome = input('Qual seu sobrenome?\n')
    idade = input('Qual sua idade?\n')

    nome_completo = nome + ' ' + sobrenome

    print(f'Seja bem vindo {nome_completo}!')
    print('Você, ' + nome_completo + ', atualmente tem ' + idade + ' anos.')
    print('Outra forma de escrever tudo isso ai em cima é... Seja bem vindo {}, você tem {} anos.'.format(nome_completo, idade))

    print(nome_completo.upper() * 7)
    print(nome_completo.lower() * 7)
    print(nome_completo.capitalize() * 7)

#chamando a função
saudacao()

#exibindo o tipo da varivel
print(type(saudacao))

#input('')

chute = input('Informe um valor: \n')
gols  = input('Informe outro valor: \n')

mensagem = 'Voce informou os valores {} e {} e esses valores são'.format(chute, gols)

if chute == gols:
    print('{} iguais.'.format(mensagem))
else:
    print('{} diferentes.'.format(mensagem))

py_compile.compile('saudacao.py')