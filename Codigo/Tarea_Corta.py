import random
import time

"""
Entrada: filas y columnas.
Salida: una matriz de números aleatorios.
Proceso: Este algoritmo genera una matriz de números aleatorios.
"""
def GenerarMatrizAleatoria(filas, columnas):
    if not (isinstance(filas, int) and isinstance(columnas, int)) or filas <= 0 or columnas <= 0:
        raise ValueError("Las filas y columnas deben ser enteros positivos.")
    # Crear una matriz vacía
    matriz = []
    # Llenar la matriz con filas de números aleatorios
    for i in range(filas):
        # Crear una fila vacía
        fila = []
        # Llenar la fila con números aleatorios
        for j in range(columnas):
            # Generar un número aleatorio y agregarlo a la fila
            fila.append(random.randint(-9, 9))
        matriz.append(fila) 
    # Retornar la matriz generada
    return matriz

"""
Entrada: Una matriz de números desordenados.
Salida: La misma matriz ordenada de menor a mayor.
Proceso: Este algoritmo saca cada lista de la matriz y llama a la funcion de ordenar listas
"""
def ordenar_matriz(Matriz):
    if not isinstance(Matriz, list):
        raise ValueError("La entrada debe ser una matriz (lista de listas).")
    # recorrer cada lista de la matriz
    for lista in range(len(Matriz)):
        if not isinstance(Matriz[lista], list):
            raise ValueError("La entrada debe ser una matriz (lista de listas).")
        # Llamar a la función de ordenamiento para cada lista
        Matriz[lista] = OrdenarListaPivot(Matriz[lista])
    # Retornar la matriz ordenada
    return Matriz

"""
Entrada: Una lista de números desordenados.
Salida: La misma lista ordenada de menor a mayor.
Proceso: Este algoritmo utiliza el método de ordenamiento QuickSort(divide y vencerás) utilizando el elemento del medio como pivote.
"""
def OrdenarListaPivot(Lista):
    # Caso base: Si la lista está vacía, retornar una lista vacía
    if not Lista:
        return []
    # Elegir el pivote
    pivot = Lista[(len(Lista) - 1)//2]
    # Dividir la lista en tres partes
    izquierda = []
    derecha = []
    iguales = []
    # Clasificar los elementos en las tres listas
    for x in Lista:
        # Los elementos menores que el pivote van a la izquierda
        if x < pivot:
            izquierda.append(x)
        # Los elementos iguales al pivote van al medio
        elif x == pivot:
            iguales.append(x)
        # Los elementos mayores que el pivote van a la derecha 
        elif x > pivot:
            derecha.append(x)
    # Recursivamente ordenar las sublistas
    return OrdenarListaPivot(izquierda) + iguales + OrdenarListaPivot(derecha)


def PruebaOrdenamiento(i, j):
    matriz=GenerarMatrizAleatoria(i, j)
    print("Matriz generada:")
    for fila in matriz:
        print(fila)
    inicio = time.perf_counter()
    ordenar_matriz(matriz)
    fin = time.perf_counter()
    print("Matriz Ordenada:")
    for fila in matriz:
        print(fila)
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")



PruebaOrdenamiento(10, 10)