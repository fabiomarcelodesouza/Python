def velocidade_media(distancia, tempo):
    velocidade = divisao(distancia, tempo)
    print(velocidade)

def soma(num1, num2):
    return num1 + num2

def divisao(num1, num2):
    return num1 / num2

def calculadora(num1, num2):
    return num1 + num2, num1 - num2

def teste_args_kwargs(arg1, arg2, arg3):
        print("arg1: ", arg1)
        print("arg2: ", arg2)
        print("arg3: ", arg3)

velocidade_media(100, 20)
velocidade_media(150, 22)
velocidade_media(200, 30)
velocidade_media(50, 3)

print(soma(7, 14))
print(calculadora(7, 14))
print(type(calculadora(7, 14)))

args = ('um', 2, 3)
teste_args_kwargs(*args)

kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um'}
teste_args_kwargs(**kwargs)