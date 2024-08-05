def encontrar_extremos(lista):
    if not lista:
        return None, None  # Devolver None si la lista está vacía

    minimo = maximo = lista[0]  # Inicializar el mínimo y máximo con el primer elemento

    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    return minimo, maximo

# Ejemplo de lista de números
numeros = [23, 45, 12, 67, 89, 34]

# Encontrar el número más pequeño y el más grande en la lista
minimo, maximo = encontrar_extremos(numeros)

# Imprimir los resultados
print("El número más pequeño en la lista es:", minimo)
print("El número más grande en la lista es:", maximo)
