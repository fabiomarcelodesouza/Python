from adivinhacao import AdivinhacaoComWhile
import forca

print('*********************************')
print('**********MENU DE JOGOS**********')
print('*********************************')
print("1. Adivinhação")
print("2. Forca")

escolha = int(input("Qual jogo quer jogar? Digite o número: "))

if escolha == 1:
    AdivinhacaoComWhile(4)
elif escolha == 2:
    forca.jogar()