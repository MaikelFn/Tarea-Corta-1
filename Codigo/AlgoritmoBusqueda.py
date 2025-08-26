import random
import time
import tracemalloc
import bisect

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

"""
Entrada: Una matriz y un valor a buscar.
Salida: True si el valor existe en la matriz, False si no.
Proceso: Se recorre la matriz buscando el valor en cada fila y columna.
"""
def existe_en_matriz(matriz, valor_buscar):
    # Validar que matriz sea tipo list y el valor a buscar un entero
    if not isinstance(matriz, list)  or not isinstance (valor_buscar,int):
        raise ValueError("matriz debe ser de tipo lista y el valor a buscar debe ser entero.")
    # Recorrer cada fila y comprobar si el valor está presente
    for fila in matriz:
        if isinstance(fila,list):
            for elemento in fila:
                if elemento == valor_buscar:
                    return True
        else:
            return "No es matriz"    
    # Si no se encontró en ninguna fila, devolver False
    return False

#-----------------------------------------------------
# BÚSQUEDA BINARIA, se utiliza en listas ordenadas
# Lo usaremos para hacer comparaciones
#-----------------------------------------------------
def busqueda_binaria_lista(matriz, valor):
    lista = [elem for fila in matriz for elem in fila]  # aplanar matriz
    lista.sort()
    idx = bisect.bisect_left(lista, valor)  # posición donde debería estar
    return idx < len(lista) and lista[idx] == valor


# Pruebas usando nuestro algoritmo de búsqueda lineal
def PruebaBusqueda(matriz, y):
    # Prueba de la función existe_en_matriz
    # matriz = GenerarMatrizAleatoria(i, j)
    inicio = time.perf_counter()
    tracemalloc.start()
    ##print("Matriz generada:") ##DESCOMENTAR SI SE QUIERE VER LA MATRIZ
    ##for fila in matriz:
        ##print(fila)
    print(f"Buscando el valor: {y}")
    resultado = existe_en_matriz(matriz, y)
    print(f"Resultado de la búsqueda: {resultado}")
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print(f"Tiempo de búsqueda: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")
    

# Pruebas usando un algoritmo de búsqueda binaria
def PruebaBusqueda2(matriz, y):
    # Prueba de la función busqueda_binaria_lista
    # matriz = GenerarMatrizAleatoria(i, j)
    inicio = time.perf_counter()
    tracemalloc.start()
    ##print("Matriz generada:") ## DESCOMENTAR SI SE QUIERE VER LA MATRIZ
    ##for fila in matriz:
        ##print(fila)
    print(f"Buscando el valor: {y}")
    resultado = busqueda_binaria_lista(matriz, y)
    print(f"Resultado de la búsqueda: {resultado}")
    memoria_actual, memoria_max = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    fin = time.perf_counter()
    print(f"Tiempo de búsqueda: {(fin - inicio):.6f} segundos")
    print(f"Memoria actual usada: {memoria_actual} KB")
    print(f"Memoria máxima usada: {memoria_max} KB")


# Funcion para ver pruebas entre ambas funciones (algoritmo lineal vs binario)
# Utilizar para comprobar funcionalidades
# i,j: dimensiones
# y:   valor a buscar
def pruebas(i,j,y):
    matriz = GenerarMatrizAleatoria(i, j)
    print ("BÚSQUEDA LINEAL\n")
    PruebaBusqueda(matriz,y)
    print ("\n")
    print ("BÚSQUEDA BINARIA\n")
    PruebaBusqueda2(matriz,y)
