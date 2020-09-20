<h1> Tp 1 - Estructura de datos - Grupo 11 <h1>

<h2> Ordenamiento Rapido y busqueda binaria </h2>

#  Binary Search (búsqueda binaria)

<p> Este algoritmo de búsqueda tiene un tiempo de ejecución que varía dependiendo de la longitud del arreglo, y su complejidad en promedio es de log(n/2), la mitad de veces que una cantidad de elementos se puede dividir en 2 hasta que llega a 1.<br>
El algoritmo consta en tomar una lista o arreglo ordenado y a partir de sus indices de inicio y fin toma el elemento del medio y lo compara con el elemento buscado, esto puede dar 3 situaciones: <p>

<ol> 
<li> El elemento buscado es el elemento medio, lo que resultaría en el final del algoritmo </li>
<li> El elemento buscado es menor al elemento medio, se vuelve a ejecutar el algoritmo manteniendo el indice de inicio pero esta vez tomando como indice final el elemento anterior al medio tomado anteriormente. Esto se repite hasta encontrar el elemento </li>
<li> El elemento buscado es mayor al elemento medio, se vuelve a ejecutar, igual al caso anterior pero esta vez se mueve el indice de inicio al elemento siguiente al elemento medio </li>
</ol>

 ***Ejemplo:*** 
 Un arreglo compuesto por = ***[2, 4, 6, 7, 8, 9, 12]*** <br>
 en un principio tiene como inicio el indice[0] elemento[2] y su final es el indice[6] elemento[12]. <p>

<p>Queremos encontrar el elemento[4] <br>
 El logaritmo toma el elemento del medio i[3] e[7] y lo compara con el buscado e[4], como el buscado es menor al medio, se vuelve a ejecutar tomando solo la porción del arreglo donde puede estar el elemento. En este caso es desde el i[0] hasta i[2] (una posición anterior al medio que ya fue comparado antes). <br>
Ahora se vuelve a ejecutar y al tomar el medio entre i[0] y i[2] nos da el i[1], al comparar el elemento que le corresponde con el buscado se da la coincidencia y finaliza el proceso. <p>
<br>

# Quicksort (ordenamiento rapido)

El ordenamiento rápido tiene una complejidad logaritmica ***O(nlog(n))***  
El algoritmo funciona tomando un elemento del arreglo a ordenar llamado ***pivote*** y lo utiliza para dividir la lista en 2 segmentos, uno con los elementos menores al pivote y oto con los mayores. quedando el pivote en su posición final. Este proceso se vuelve a repetir en cada uno de los segmentos que va generando hasta que el arreglo queda ordenado. 
