import numpy as np

# Criando um array com os números inteiros de 0 a 20
array_int = np.arange(0, 21)

# Convertendo o array para o tipo float
array_float = array_int.astype(float)

# Exibindo o resultado
print("Array original (inteiros):")
print(array_int)

print("\nArray convertido para float:")
print(array_float)
