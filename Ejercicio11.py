def generar_pares(minimo, maximo):
    pares = [num for num in range(minimo, maximo + 1) if num % 2 == 0]
    return pares

# Definir el rango
minimo_valor = 1
maximo_valor = 100

# Generar la lista de números pares
numeros_pares = generar_pares(minimo_valor, maximo_valor)

# Imprimir la lista de números pares
print("Lista de números pares entre 1 y 100:")
print(numeros_pares)


