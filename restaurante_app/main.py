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



while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        codigo = input("Código del producto: ")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: ").replace(",", "."))

        producto = Producto(codigo, nombre, precio)

        if restaurante.registrar_producto(producto):
            print("\nProducto registrado correctamente.")
        else:
            print("\nYa existe un producto con ese código.")

    elif opcion == "2":
        codigo = input("Código de la bebida: ")
        nombre = input("Nombre de la bebida: ")
        precio = float(input("Precio: ").replace(",", "."))
        tamanio = input("Tamaño: ")

        bebida = Bebida(codigo, nombre, precio, tamanio)

        if restaurante.registrar_producto(bebida):
            print("\nBebida registrada correctamente.")
        else:
            print("\nYa existe un producto con ese código.")

    elif opcion == "3":
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")

        cliente = Cliente(identificacion, nombre)

        if restaurante.registrar_cliente(cliente):
            print("\nCliente registrado correctamente.")
        else:
            print("\nYa existe un cliente con esa identificación.") 


    elif opcion == "4":
        restaurante.listar_productos()



    elif opcion == "5":
        restaurante.listar_clientes()   


    elif opcion == "6":
        print("\nGracias por utilizar el sistema.")
        break           


    else:
        print("\nOpción no válida.")