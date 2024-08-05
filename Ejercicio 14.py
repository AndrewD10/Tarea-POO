def calcular_media(lista):
    if not lista:
        return None  # Manejar el caso de lista vacía

    suma = sum(lista)
    cantidad = len(lista)
    media = suma / cantidad
    return media

# Ejemplo de lista de números
numeros = [10, 20, 30, 40, 50]

# Calcular la media de la lista de números
resultado_media = calcular_media(numeros)

# Imprimir el resultado
print("La media aritmética de la lista es:", resultado_media)
