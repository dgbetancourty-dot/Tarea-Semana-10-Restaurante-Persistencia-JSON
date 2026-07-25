from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante()


def mostrar_menu():
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")


def registrar_producto():
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: ").replace(",", "."))

    producto = Producto(codigo, nombre, precio)

    if restaurante.registrar_producto(producto):
        print("\nProducto registrado correctamente.")
    else:
        print("\nYa existe un producto con ese código.")


def registrar_bebida():
    codigo = input("Código de la bebida: ")
    nombre = input("Nombre de la bebida: ")
    precio = float(input("Precio: ").replace(",", "."))
    tamanio = input("Tamaño: ")

    bebida = Bebida(codigo, nombre, precio, tamanio)

    if restaurante.registrar_producto(bebida):
        print("\nBebida registrada correctamente.")
    else:
        print("\nYa existe un producto con ese código.")


def registrar_cliente():
    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")

    cliente = Cliente(identificacion, nombre)

    if restaurante.registrar_cliente(cliente):
        print("\nCliente registrado correctamente.")
    else:
        print("\nYa existe un cliente con esa identificación.")


def listar_productos():
    restaurante.listar_productos()


def listar_clientes():
    restaurante.listar_clientes()


def main():

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            registrar_bebida()

        elif opcion == "3":
            registrar_cliente()

        elif opcion == "4":
            listar_productos()

        elif opcion == "5":
            listar_clientes()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()