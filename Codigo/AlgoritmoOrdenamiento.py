import random
import time
import tracemalloc

"""
Entrada: Una lista de números desordenados.
Salida: La misma lista ordenada de menor a mayor.
Este algoritmo se utilizo solo para la comparativa.
"""
def BubleSort(Matriz):
    for Lista in Matriz:
        n = len(Lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if Lista[j] > Lista[j+1]:
                    Lista[j], Lista[j+1] = Lista[j+1], Lista[j]
    return Matriz

"""
Entrada: Una lista de números desordenados.
Salida: La misma lista ordenada de menor a mayor.
Proceso: Este algoritmo utiliza el método de ordenamiento QuickSort(divide y vencerás) utilizando el elemento del medio como pivote.
"""
def OrdenarListaQuickSort(Lista):
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
    return OrdenarListaQuickSort(izquierda) + iguales + OrdenarListaQuickSort(derecha)

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
        Matriz[lista] = OrdenarListaQuickSort(Matriz[lista])
    # Retornar la matriz ordenada
    return Matriz

"""
Entrada: Dos enteros que representan las dimensiones de la matriz.
Salida: Una matriz de enteros aleatorios.
Proceso: Se generan números aleatorios para llenar la matriz.
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
            fila.append(random.randint(-100, 100))
        matriz.append(fila) 
    # Retornar la matriz generada
    return matriz

def PruebaOrdenamiento():

    # Prueba de Ordenamiento por QuickSort con 100 Elementos
    matriz=GenerarMatrizAleatoria(10, 10)
    inicio = time.perf_counter()
    tracemalloc.start()
    ordenar_matriz(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento QuickSort")
    print("Cantidad de elementos: 100")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")


    # Prueba de Ordenamiento por Burbuja con 100 Elementos
    matriz=GenerarMatrizAleatoria(10, 10)
    inicio = time.perf_counter()
    tracemalloc.start()
    BubleSort(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento Burbuja")
    print("Cantidad de elementos: 100")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")


    # Prueba de Ordenamiento por QuickSort con 1024 Elementos
    matriz=GenerarMatrizAleatoria(32, 32)
    inicio = time.perf_counter()
    tracemalloc.start()
    ordenar_matriz(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento QuickSort")
    print("Cantidad de elementos: 1024")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")

    # Prueba de Ordenamiento por Burbuja con 1024 Elementos
    matriz=GenerarMatrizAleatoria(32, 32)
    inicio = time.perf_counter()
    tracemalloc.start()
    BubleSort(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento Burbuja")
    print("Cantidad de elementos: 1024")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")

    # Prueba de Ordenamiento por QuickSort con 10000 Elementos
    matriz=GenerarMatrizAleatoria(100, 100)
    inicio = time.perf_counter()
    tracemalloc.start()
    ordenar_matriz(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento QuickSort")
    print("Cantidad de elementos: 10000")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")

    # Prueba de Ordenamiento por Burbuja con 10000 Elementos
    matriz=GenerarMatrizAleatoria(100, 100)
    inicio = time.perf_counter()
    tracemalloc.start()
    BubleSort(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento Burbuja")
    print("Cantidad de elementos: 10000")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")

    # Prueba de Ordenamiento por QuickSort con 100489 Elementos
    matriz=GenerarMatrizAleatoria(317, 317)
    inicio = time.perf_counter()
    tracemalloc.start()
    ordenar_matriz(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento QuickSort")
    print("Cantidad de elementos: 100489")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print("\n")

    # Prueba de Ordenamiento por Burbuja con 100489 Elementos
    matriz=GenerarMatrizAleatoria(317, 317)
    inicio = time.perf_counter()
    tracemalloc.start()
    BubleSort(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento Burbuja")
    print("Cantidad de elementos: 100489")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")

    # Prueba de Ordenamiento por QuickSort con 1000000 Elementos
    matriz=GenerarMatrizAleatoria(1000, 1000)
    inicio = time.perf_counter()
    tracemalloc.start()
    ordenar_matriz(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento QuickSort")
    print("Cantidad de elementos: 1000000")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")

    for i in range(5):
        print(f"{matriz[i]}")

    # Prueba de Ordenamiento por Burbuja con 1000000 Elementos
    """matriz=GenerarMatrizAleatoria(1000, 1000)
    inicio = time.perf_counter()
    tracemalloc.start()
    BubleSort(matriz)
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print("Prueba de Ordenamiento Burbuja")
    print("Cantidad de elementos: 1000000")
    print(f"Tiempo de ordenamiento: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    print("\n")"""

PruebaOrdenamiento()