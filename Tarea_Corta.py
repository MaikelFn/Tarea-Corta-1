import random
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
