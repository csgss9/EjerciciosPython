try:  # debajo bloque que puede traer un error

    n1 = int(input("ingrese primer numero: "))
    n2 = int(input("ingrese segundo numero: "))

    if n1 > n2:
        print(f'{n1} es mayor que {n2}')
    elif n2 > n1:
        print(f'{n2} es mayor que {n1}')
    else:
        print('ambos numeros son iguales')

except ValueError:  # manejo del error
    print('Debe escribir un valor numerico')
