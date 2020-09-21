import numpy as np


# ordena y busca
# recibe un arreglo y un elemento a buscar
# ordena el arreglo con el metodo quicksort y retorna el indice
def ordenaBusca(arreglo, elemento):
    quicksort(arreglo)
    return binarySearch(arreglo, elemento)


# Busqueda binaria
# recibe un arreglo y un elemento a buscar. y retorna el indice correspondiente
def binarySearch(arreglo, elemento):
    return binarySearchAux(arreglo, elemento, 0, len(arreglo) - 1)


# auxiliar para la busqueda binaria
# recibe un arreglo, un elemento, y los indices minimo y maximo donde se hara la busqueda
# retorna el indice del elemnto
def binarySearchAux(arreglo, elemento, indiceIzq, indiceDer):
    medio = (indiceIzq + indiceDer) // 2
    resultado = medio
    if arreglo[medio] > elemento:
        resultado = binarySearchAux(arreglo, elemento, indiceIzq, medio - 1)
    elif arreglo[medio] < elemento:
        resultado = binarySearchAux(arreglo, elemento, medio + 1, indiceDer)
    else:
        resultado = medio
    return resultado


# auxiliar de particion para quicksort
# recibe un arreglo, un indice de inicio y uno de fin
# asigna un pivote y separa la lista entre los menores y los mayores a ese pivote, dejando el pivote en su posicion final
def particionado(arreglo, inicio, fin):
    pivot = arreglo[inicio]
    izq = inicio + 1
    der = fin
    terminado = False

    while terminado == False:
        while izq <= der and arreglo[izq] <= pivot:
            izq += 1

        while izq <= der and arreglo[der] >= pivot:
            der -= 1

        if der < izq:
            terminado = True
        else:
            arreglo[izq], arreglo[der] = arreglo[der], arreglo[izq]

    arreglo[inicio], arreglo[der] = arreglo[der], arreglo[inicio]
    return der


# ordenamiento rapido
# recibe un arreglo y lo ordena de menor a mayor
def quicksort(arreglo):
    quicksortAux(arreglo, 0, len(arreglo)-1)


# auxiliar para ordenamiento rapido
# recibe un arreglo, un indice de inicio y uno de fin
# ordena el arreglo de menor a mayor
def quicksortAux(arreglo, inicio, fin):
    if inicio < fin:
        puntoParticion = particionado(arreglo, inicio, fin)
        quicksortAux(arreglo, inicio, puntoParticion - 1)
        quicksortAux(arreglo, puntoParticion + 1, fin)





arr = np.array([7, 4, 5, 2, 3, 6])

#sin ordenamiento ---> indice[2]
print(binarySearch(arr, 5))

#con ordenamiento ---> indice[3]
print(ordenaBusca(arr, 5))

