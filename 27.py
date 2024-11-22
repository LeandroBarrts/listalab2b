import numpy as np

# Definindo a matriz de transformação 2x2
matriz = np.array([[2, 3],
                   [1, 4]])

# Definindo o vetor v
v = np.array([1, 2])

# Aplicando a transformação linear (multiplicação da matriz pelo vetor)
resultado = np.dot(matriz, v)

# Exibindo o resultado
print("Vetor após a transformação:")
print(resultado)
