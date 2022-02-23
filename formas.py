#from math import pi

from math import pi

class Forma():
    #PI = 3.1415
    def area(self):
        # solo definimos la estructura. No podemos saber el area sin conocer la forma
        pass
    
    def perimetro(self):
        # solo definimos la estructura. No podemos saber el perimetro sin conocer la forma
        pass

    def __str__(self) -> str:
        # imprime el nombre del objeto
        return type(self).__name__


class Circulo(Forma):
    # clase que hereda de Forma, para implementar los circulos
    def __init__(self, radio=1) -> None:
        if type(radio) in (int, float) and radio >= 0: 
            self.__radio = radio
        else:
            raise Exception('El radio debe ser un numero positivo')
    
    def area(self):
        return pi * self.__radio * self.__radio

    def perimetro(self):
        return 2 * pi * self.__radio


class Rectangulo(Forma):
    def __init__(self, base=1, altura=1) -> None:
        self.__base = base
        self.__altura = altura
    
    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2 * self.__base + 2 * self.__altura

    

class Cuadrado(Rectangulo):
    def __init__(self, lado=1) -> None:
        super().__init__(lado, lado)

    """ def area(self):
        return super().area() """
        