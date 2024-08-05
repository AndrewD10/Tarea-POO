def factorial(n):
    if n < 0:
        return None  # Manejar números negativos (factorial no está definido para números negativos)
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplos de cálculo de factorial
numero = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")

# Para un número negativo 
numero_negativo = int(input("Ingrese un número negativo para calcular su factorial: "))
resultado_factorial_negativo = factorial(numero_negativo)
print(f"El factorial de {numero_negativo} es: {resultado_factorial_negativo}")