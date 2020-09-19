import numpy as np

# Busqueda binaria
def binarySearch(arreglo, elemento, indiceIzq, indiceDer):
    medio = (indiceIzq + indiceDer) // 2
    resultado = medio
    if arreglo[medio] > elemento:
        resultado = binarySearch(arreglo, elemento, indiceIzq, medio-1)
    elif arreglo[medio] < elemento:
        resultado = binarySearch(arreglo, elemento, medio+1, indiceDer)
    else:
        resultado = medio
    return resultado




# auxiliar de particion para quicksort
def particionado(arreglo, indiceMenor, indiceMayor):
    pivot = arreglo[indiceMenor]
    izq = indiceMenor + 1
    der = indiceMayor

    while True:
        while izq <= der and arreglo[izq] <= pivot:
            izq += 1

        while izq <= der and arreglo[der] >= pivot:
            der -= 1

        if der < izq:
            break
        else:
            arreglo[izq], arreglo[der] = arreglo[der], arreglo[izq]

    arreglo[indiceMenor], arreglo[der] = arreglo[der], arreglo[indiceMenor]
    return der

#ordenamiento rapido
def quicksort(arreglo, indiceMenor, indiceMayor):
    if indiceMenor < indiceMayor:
        pivote = particionado(arreglo, indiceMenor, indiceMayor)
        quicksort(arreglo, indiceMenor, pivote-1)
        quicksort(arreglo, pivote+1, indiceMayor)
    return arreglo



arr = np.array([7, 2, 3, 4, 5, 6])
print(quicksort(arr, 0, 5))
