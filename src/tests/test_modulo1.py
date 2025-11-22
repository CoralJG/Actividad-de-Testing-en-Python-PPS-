# tests/test_modulo1.py
import unittest
from modulo1.funciones import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    # Lista de casos de prueba con cadenas propias y resultado esperado
    def setUp(self):
        self.casos_prueba = [
            ("", True),
            ("a", True),
            ("Ana", True),
            ("A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá", True),
            ("Anita lava la tina", True),
            ("Amor a Roma", True),
            ("Atar a la rata", True),
            ("La ruta nos aportó otro paso natural", True),
            ("Este no es un palíndromo", False),
            ("S o l", False),
            ("Camarón", False),
            ("No 'se' pero si sé", False),
            ("A mi perrita Neya le gusta pasear por el campo y ver su camión favorito pasar", False),
            ("Coral es la mejor", False),
        ]

    # Test que recorre todos los casos definidos, usando subTest para identificar cada uno individualmente
    # Controla excepciones para que cualquier error en la función se refleje en la prueba
    def test_es_palindromo(self):
        # Testea cada cadena y compara el resultado con el esperado
        for cadena, esperado in self.casos_prueba:
            with self.subTest(cadena=cadena):
                try:
                    resultado = esPalindromo(cadena)  # Invoca la función bajo prueba
                    self.assertEqual(resultado, esperado)  # Verifica que el resultado coincida con lo esperado
                except Exception as e:
                    self.fail(f"La función lanzó una excepción inesperada: {e}")

    # Test específico para cadenas largas, asegurando que la función maneje bien grandes volúmenes de datos
    def test_cadena_larga(self):
        # Crear cadena palíndroma muy larga
        base = "La ruta nos aportó otro paso natural"
        cadena_larga = base * 1000
        try:
            self.assertTrue(esPalindromo(cadena_larga)) 
        except Exception as e:
            self.fail(f"La función lanzó una excepción inesperada: {e}")
        # Crear cadena no palíndroma muy larga
        cadena_no_palindromo = "Coral" * 10000 
        try:
            self.assertFalse(esPalindromo(cadena_no_palindromo))
        except Exception as e:
            self.fail(f"La función lanzó una excepción inesperada: {e}")


if __name__ == "__main__":
    unittest.main()