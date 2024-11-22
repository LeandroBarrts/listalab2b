import numpy as np

array = np.random.rand(20)

media = np.mean(array)
desvio_padrao = np.std(array)
maximo = np.max(array)
minimo = np.min(array)

print("Array:", array)
print("Média:", media)
print("Desvio padrão:", desvio_padrao)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)
