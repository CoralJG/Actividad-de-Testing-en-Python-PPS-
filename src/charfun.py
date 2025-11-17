
r""""
Programa que determina si una cadena proporcionada por el 
usuario es palíndroma. Para ello se preguntará por teclado al 
usuario tantas veces como quiera hasta que escriba la palabra salir. 

Ultima Modificación. 17/11/2025
Autor. Coral Jácome García
Dependencias. Unicodedata

"""
import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.

    """
    # Convertir la cadena a minúsculas y eliminar caracteres no alfabéticos
    cadena_limpia = ''.join(char.lower() for char in cadena if char.isalnum())
    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

# Proteger para que no se ejecute en tests
if __name__ == "__main__":
    while True:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
        if frase.lower() == "salir":
            print("Programa finalizado.")
        else:
            # Comprobar si es palíndromo
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")