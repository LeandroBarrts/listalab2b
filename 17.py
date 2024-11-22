import numpy as np

# Criando uma matriz quadrada 3x3 aleatória
matriz = np.random.rand(3, 3)

# Calculando o determinante da matriz
determinante = np.linalg.det(matriz)

# Verificando se o determinante é diferente de zero para garantir que a matriz é invertível
if determinante != 0:
    # Calculando a inversa da matriz
    inversa = np.linalg.inv(matriz)
    print("Matriz original:")
    print(matriz)
    print("\nDeterminante:", determinante)
    print("\nInversa da matriz:")
    print(inversa)
else:
    print("A matriz não é invertível, pois o determinante é zero.")
