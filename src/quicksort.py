import numpy as np

def binarySearch(arreglo, elemento, indiceIzq, indiceDer):
    medio = (indiceIzq + indiceDer) // 2

    if arreglo[medio] > elemento:
        binarySearch(arreglo, elemento, indiceIzq, medio-1)
    elif arreglo[medio] < elemento:
        binarySearch(arreglo, elemento, medio+1, indiceDer)
    else:
        return medio


arr = np.array([1, 2, 3, 4, 5, 6])
print(binarySearch(arr, 5, 0, 5))