from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto: Producto) -> bool:
        for producto_existente in self.productos:
            if producto_existente.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        for cliente_existente in self.clientes:
            if cliente_existente.identificacion == cliente.identificacion:
                return False

        self.clientes.append(cliente)
        return True

    def listar_productos(self):
        print("Entré al método listar_productos")

        if not self.productos:
            print("\nNo existen productos registrados.")
            return

        print("\n===== LISTA DE PRODUCTOS =====")

        for producto in self.productos:
            producto.mostrar_informacion()
            print("-" * 30)

    def listar_clientes(self):
        print("Entré al método listar_clientes")

        if not self.clientes:
            print("\nNo existen clientes registrados.")
            return

        print("\n===== LISTA DE CLIENTES =====")

        for cliente in self.clientes:
            cliente.mostrar_informacion()
            print("-" * 30)