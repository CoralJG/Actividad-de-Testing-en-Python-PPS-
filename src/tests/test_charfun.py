
r""""
Programa que determina si una cadena proporcionada por el 
usuario es palíndroma. Para ello se preguntará por teclado al 
usuario tantas veces como quiera hasta que escriba la palabra salir. 

Ultima Modificación. 17/11/2025
Autor. Coral Jácome García
Dependencias. Unittest

"""

import unittest 
from src.charfun import esPalindromo

class TestEsPalindromo_CoralJG(unittest.TestCase):

    """
    Clase que testea si una cadena es palíndroma.

    """
    def test_esPalindromo(self):
        # Cadena de palíndromos 'True' y no palíndromos 'False'
        tests = [("", True), ("1", True), ("a", True), ("Esto no es un palíndromo", False), ("S o l", False), ("Coral", False)] 
        # Comprobar si es palíndromo
        for cadena, esperada in tests:
           with self.subTest(cadena=cadena):
               self.assertEqual(esPalindromo(cadena), esperada)

if __name__ == "__main__":
    unittest.main()