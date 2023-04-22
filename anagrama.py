palabra_1 = input("Ingrese la primera palabra")
palabra_2 = input("Ingrese la segunda palabra")


def es_anagrama(palabra_1, palabra_2):
    palabra_1 = sorted(palabra_1)
    palabra_2 = sorted(palabra_2)

    if palabra_1 == palabra_2:
        return True
    else:
        return False


resultado = es_anagrama(palabra_1, palabra_2)
print(resultado)
