palabras = ['Antonio', 'Felipe', 'Luis',
            'Carlos', 'Fernando', 'Lu', 'Paul', 'Jorge']
n = int(input('Ingrese la cantidad de letras de las palabras que desea: '))
lista = []


# def filtrar_palabras(palabras, n):
#     for palabra in palabras:
#         if len(palabra) > n:
#             lista.append(palabra)

# Ahora con list comprenhensions
[lista.append(palabra) for palabra in palabras if len(palabra) > n]
# filtrar_palabras(palabras, n)
print(lista)
