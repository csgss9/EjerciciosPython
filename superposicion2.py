lista1 = [1, 6, 8, 4, 0, 5]
lista2 = [3, 7, 8, 2, 5, 9]


def superposicion(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    return set1 & set2


resultado = superposicion(lista1, lista2)
print(resultado)
