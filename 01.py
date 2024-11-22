import numpy as np

# Criando um array unidimensional (1D) contendo os números de 1 a 10
array_1d = np.arange(1, 11)

# Exibindo o array unidimensional antes da transformação
print("Array unidimensional original:")
print(array_1d)

# Transformando o array 1D em um array 2D com 2 linhas e 5 colunas
array_2d = array_1d.reshape(2, 5)

# Exibindo o array bidimensional resultante
print("\nArray bidimensional após a transformação:")
print(array_2d)
