clave_maestra = [1, 2, 3, 4, 5, 6]
clave_par = []
clave_impar = []


def buscar_clave():
    for numero in clave_maestra:
        if numero % 2 == 0:
            clave_par.append(numero)
        else:
            clave_impar.append(numero)
    return clave_impar, clave_par


buscar_clave()
print(f'Clave 1 es {clave_impar} y clave 2 es {clave_par}')
