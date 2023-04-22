lista1 = [1, 6, 8, 4, 0, 5]
lista2 = [3, 7, 8, 2, 5, 9]
lista3 = []


def superposicion(lista1, lista2):
    for i in lista1:
        for e in lista2:
            if i == e:
                lista3.append(i)

    if lista3:
        print(f"los elementos{lista3} son iguales en ambas listas")
        return True
    else:
        print('No hay elementos iguales')
        return False


resultado = superposicion(lista1, lista2)
print(resultado)
