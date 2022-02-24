from random import randint
from formas import Circulo, Cuadrado, Rectangulo

CIRCULO = 1
RECTANGULO = 2
CUADRADO = 3






class Manejador():
    @classmethod
    def get_figura(self, num):
        if num == CIRCULO:
            return Circulo(randint(1,10))
        if num == CUADRADO:
            return Cuadrado(randint(1,10))
        if num == RECTANGULO:
            return Rectangulo(randint(1,10), randint(1,10))
        raise Exception('El numero debe estar entre 1 y 3')

# =============================================================================

figuras = []
txt = []
for i in range(5):
    f = Manejador.get_figura(randint(1,3))
    figuras.append(f)
    txt.append(f'La figura {f} tiene un área de {f.area()} y un perimetro de {f.perimetro()}')


print('\n'.join(txt))