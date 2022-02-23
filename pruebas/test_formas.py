'''
Batería de test unitarios para probar las clases del archivo formas.py
'''
import unittest
from formas import Circulo, Cuadrado, Forma
from math import pi

class TestClaseForma(unittest.TestCase):
    # Tests para probar la clase Forma 
    def test_existencia(self):
        f = Forma()
        self.assertIsNotNone(f)

    def test_nombre_forma(self):
        f = Forma()
        self.assertEqual(f.__str__(), 'Forma')

    
class TestClaseCirculo(unittest.TestCase):
    # Tests para probar la clase Circulo
    def test_existencia(self):
        c = Circulo()
        self.assertIsNotNone(c) 

    def test_circulo_radio_1_perimetro_2pi(self):
        c = Circulo(1)
        resp = c.perimetro()
        self.assertEqual(resp, 2*pi)

    def test_radio_negativo_da_error(self):
        with self.assertRaises(Exception):
            c = Circulo(-1)


class TestClaseCuadrado(unittest.TestCase):
    def test_existencia(self):
        pass

    def test_lado_1_perimetro_4(self):
        cu = Cuadrado(1)
        resp = cu.perimetro()
        self.assertEqual(resp, 4)
        
    def test_area_lado_1_dev_1(self):
        cu = Cuadrado(1)
        resp = cu.area()
        self.assertEqual(resp, 1)
        

    