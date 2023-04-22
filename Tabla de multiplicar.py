numero = int(input("¿Que tabla de multiplicar desea? "))

for i in range(1, 11):
    multi = numero * i
    print(f'{numero} x {i} = {multi}')
