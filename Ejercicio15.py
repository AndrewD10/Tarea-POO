def es_palindromo(texto):
    # Eliminar espacios y convertir a minúsculas
    texto_limpio = ''.join(char.lower() for char in texto if char.isalnum())
    # Verificar si el texto limpio es igual a su reverso
    return texto_limpio == texto_limpio[::-1]

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Determinar si la cadena es un palíndromo
if es_palindromo(cadena):
    print("La cadena ingresada es un palíndromo.")
else:
    print("La cadena ingresada no es un palíndromo.")
