from modelos.producto import Producto


class Bebida(Producto):
    def __init__(self, codigo, nombre, precio, tamanio):
        super().__init__(codigo, nombre, precio)
        self._tamanio = tamanio

    @property
    def tamanio(self):
        return self._tamanio

    def mostrar_informacion(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Tamaño: {self._tamanio}")