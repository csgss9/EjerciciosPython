class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

# Metodos

    def area(self):
        area = self.ancho * self.alto
        return area

    def perimetro(self):
        perimetro = (self.ancho + self.alto) * 2
        return perimetro

    # Otra manera de imprimir atributos
    # def __str__(self):
        # return f' El alto de su cuadrado es {self.alto} y el ancho {self.ancho}'


ancho = int(input("Ingrese el ancho del rectangulo"))
alto = int(input("Ingrese el alto del rectangulo"))


# # Objetos
rectangulo_1 = Rectangulo(ancho, alto)

# # print(rectangulo_1.alto) #para imprimir un atributo
# manera de imprimir 1
print(f'El area del rectangulo es {rectangulo_1.area()}')
print('El perimetro del rectangulo es ',rectangulo_1.perimetro())  # manera de imprimir 2
