def invertir_lista(lista):
    lista_invertida = lista[::-1]  # Utilizar slicing para invertir la lista
    return lista_invertida

# Lista de números
numeros = [23, 45, 12, 67, 89, 34]

# Invertir la lista de números
numeros_invertidos = invertir_lista(numeros)

# Imprimir la lista invertida
print("Lista original:", numeros)
print("Lista invertida:", numeros_invertidos)