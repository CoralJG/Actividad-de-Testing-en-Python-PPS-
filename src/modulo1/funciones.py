# Funciones auxiliares de la función principal 'esPalindromo' (lógica)
# modulo1/funciones.py
import unicodedata

def esPalindromo(cadena):
    """
    Verifica si la cadena es palíndroma.
    Ignora espacios, puntuación, mayúsculas, tildes y diéresis.

    Parámetros:
    cadena (str): La cadena de texto a verificar.

    Retorna:
    bool: 'True' si la cadena es un palíndromo, 'False' en caso contrario.
    """
    # Normaliza la cadena usando NFD para separar caracteres base y diacríticos
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    # Elimina los caracteres diacríticos (categoría 'Mn' en unicodedata)
    cadena_sin_diacriticos = ''.join(
        c for c in cadena_normalizada if unicodedata.category(c) != 'Mn'
    )
    # Convierte la cadena a minúsculas y elimina caracteres no alfanuméricos
    cadena_limpia = ''.join(c.lower() for c in cadena_sin_diacriticos if c.isalnum())
    # Compara la cadena limpia con su reverso para determinar si es palíndroma
    return cadena_limpia == cadena_limpia[::-1]



