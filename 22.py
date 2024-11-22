import numpy as np

# Definindo o array com os valores x
x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])

# Calculando o seno e o cosseno de cada valor
seno = np.sin(x)
cosseno = np.cos(x)

# Exibindo os resultados
print("Valores de x:", x)
print("\nSeno de x:", seno)
print("\nCosseno de x:", cosseno)

