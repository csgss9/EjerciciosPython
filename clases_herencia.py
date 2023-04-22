class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Maestro(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado


class Estudiante(Persona):
    def __init__(self, nombre, edad, codigo):
        super().__init__(nombre, edad)
        self.codigo = codigo

# Crear subclase:


class Universitario(Estudiante):
    def __init__(self, nombre, edad, codigo, carrera):
        super().__init__(nombre, edad, codigo)
        self.carrera = carrera

    def __str__(self):
        return f' Nombre: {self.nombre}, edad: {self.edad}, codigo: {self.codigo}, carrera: {self.carrera}'


Universitario_1 = Universitario('Juan', 25, 1414, 'Medicina')
print(Universitario_1)
# print(f'{Universitario_1.nombre} {Universitario_1.edad} {Universitario_1.codigo} {Universitario_1.carrera}')
