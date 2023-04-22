"""
Este módulo contiene una función que toma un número entero y un caracter
y devuelve el caracter repetido n veces.
"""

veces = int(input('¿Cuantas veces desea imprimir la letra?'))
caracter = input('¿Cual letra desea imprimir?')


def generar_n_caracteres(veces, caracter):
    return caracter * veces


resultado = generar_n_caracteres(veces, caracter)
print(resultado)
