
class Product():
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return self.name

    def purchase(self):
        self.stock -= 1
        return self.stock

    def detail(self):
        detail = f'Nombre: {self.name} Precio: {self.price} Cantidad: {self.stock} Categoria: {self.category}'
        return detail


class Category():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Relacion de clases:
comidas = Category('Comidas')

# Instancia de Objetos
papa_frita = Product('Papa Frita', 250, 100, comidas)
print(papa_frita)
print(papa_frita.purchase())
print(papa_frita.detail())

coca_cola = Product('Coca-Cola', 500, 10, comidas)
print(coca_cola)
print(coca_cola.purchase())
print(coca_cola.detail())
