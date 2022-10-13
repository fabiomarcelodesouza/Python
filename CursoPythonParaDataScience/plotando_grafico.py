#%%
import matplotlib.pyplot as plt
from random import randrange, seed

#seed(10)
notas_matematica = []

for nota in range(8):
    nota = randrange(1, 11, 1)
    notas_matematica.append(nota)

x = list(range(1, 9))
y = notas_matematica
plt.plot(x, y, marker = 'o')
plt.title("Notas de Matemática")
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
# %%
