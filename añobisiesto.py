# El año 2020 cumple con esta regla, ya que es divisible por 4 (es decir, 2020/4 = 505),
# y no es un múltiplo de 100 pero sí es un múltiplo de 400 (es decir, 2020/100 = 20.2 y 2020/400 = 5)

año = int(input('Ingrese año: '))


def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        print('Este año es bisiesto')
    else:
        print('No es año bisiesto')


es_bisiesto(año)
