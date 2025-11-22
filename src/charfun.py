r""""
Programa que determina si una cadena proporcionada por el 
usuario es palíndroma. Para ello se preguntará por teclado al 
usuario tantas veces como quiera hasta que escriba la palabra salir. 

Ultima Modificación. 22/11/2025
Autor. Coral Jácome García
Dependencias. -

"""

# Importamos la función esPalindromo desde el módulo1
from modulo1.funciones import esPalindromo
# Importamos la clase GestorPalindromos desde el módulo2
from modulo2.clases import GestorPalindromos

def main():
    """
    Función principal que crea un gestor de palíndromos y ejecuta el programa.
    """
    # Se crea una instancia de GestorPalindromos pasando la función esPalindromo
    gestor = GestorPalindromos(esPalindromo)
    # Se ejecuta el método que inicia la interacción con el usuario
    gestor.ejecutar()

# Si se ejecuta el programa directamente (python .\charfun.py), se llama a main()
if __name__ == "__main__":
    main()

