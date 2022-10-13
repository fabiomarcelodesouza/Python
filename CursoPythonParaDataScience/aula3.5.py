def verifica_se_tem_idade_para_dirigir(lista):
    for cont in range(0, len(lista)):
        if lista[cont] >= 18:
            print('O condutor {} tem {} anos e já pode fazer merda'.format(cont + 1, lista[cont]))
        else:
            print('O condutor {} tem {} anos e tem que esperar com a bunda sentada na cadeira'.format(cont + 1, lista[cont]))

idades = []

for cont in range(1,5):
    idades.append(int(input('Informe a idade do condutor numero {}: '.format(cont))))

verifica_se_tem_idade_para_dirigir(idades)

