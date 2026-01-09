# Exemplo de matriz 2x3
matriz = [
    [2, 1, 0],
    [-4, 1, 2]
]
print (len(matriz), len(matriz[0]))
# Realizando a transposição
transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print("Matriz Original:", matriz, sep="\n")
print("Matriz Transposta:", transposta, sep="\n")