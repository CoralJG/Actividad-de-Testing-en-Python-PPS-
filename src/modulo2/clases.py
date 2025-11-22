# Clases auxiliares de la función principal 'esPalindromo' (tests)
# modulo2/clases.py
"""
Clase que gestiona la entrada de usuario para verificar 
frases palíndromas usando la función esPalindromo.
"""
class GestorPalindromos:
    """
    Inicializa el gestor con una función que verifica palíndromos.
    """
    def __init__(self, funcion_palindromo):
        self.funcion_palindromo = funcion_palindromo

    def ejecutar(self):
        """
        Ejecutar el bucle principal y solicitar frases al usuario
        hasta que se escriba 'salir'. Muestra si una frase es palíndroma.
        """
        while True:
            frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
            if frase.lower() == "salir":
                print("Programa finalizado.")
                break
            if self.funcion_palindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")



