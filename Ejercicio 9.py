import random

def generar_matriz(filas, columnas, minimo, maximo):
    matriz = [[random.randint(minimo, maximo) for _ in range(columnas)] for _ in range(filas)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()  

# Definir parámetros de la matriz
filas = 3
columnas = 4
minimo_valor = 1
maximo_valor = 100

# Generar la matriz de números aleatorios
matriz_numeros = generar_matriz(filas, columnas, minimo_valor, maximo_valor)

# Imprimir la matriz generada
print("Matriz de números aleatorios:")
imprimir_matriz(matriz_numeros)
