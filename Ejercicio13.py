def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = None
    if num2 != 0:
        division = num1 / num2
    return suma, resta, multiplicacion, division

# Solicitar al usuario que ingrese dos números
try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    # Calcular resultados
    suma, resta, multiplicacion, division = operaciones_basicas(numero1, numero2)

    # Imprimir resultados
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    if division is not None:
        print(f"División: {division}")
    else:
        print("División: No se puede dividir por cero.")

except ValueError:
    print("Error: Por favor, ingrese valores numéricos válidos.")