import numpy as np

# Criando um array bidimensional com as notas dos 5 alunos em 4 provas
notas = np.array([
    [7, 8, 9, 6],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [6, 7, 8, 9],
    [8, 9, 7, 8]
])

# Calculando a média de cada aluno (média das linhas)
media_alunos = np.mean(notas, axis=1)

# Calculando a média de cada prova (média das colunas)
media_provas = np.mean(notas, axis=0)

# Exibindo os resultados
print("Média de cada aluno:", media_alunos)
print("Média de cada prova:", media_provas)
