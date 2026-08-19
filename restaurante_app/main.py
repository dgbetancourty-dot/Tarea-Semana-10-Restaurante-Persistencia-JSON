from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


restaurante = Restaurante()
archivo_servicio = ArchivoServicio("datos/productos.json")

productos_guardados = archivo_servicio.cargar_productos()
restaurante.cargar_productos(productos_guardados)


OPCIONES_MENU = (
    "Registrar producto",
    "Registrar bebida",
    "Registrar usuario",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Mostrar categorías",
    "Listar usuarios",
    "Salir"
)


def leer_precio(mensaje: str) -> float:
    while True:
        try:
            precio = float(input(mensaje).replace(",", "."))

            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue

            return precio

        except ValueError:
            print("Ingrese un precio válido.")


def guardar_productos() -> None:
    productos = restaurante.obtener_productos()

    if archivo_servicio.guardar_productos(productos):
        print("Los cambios fueron guardados en productos.json.")
    else:
        print("No fue posible guardar los cambios.")


def registrar_producto() -> None:
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    precio = leer_precio("Precio: $")
    categoria = input("Categoría: ").strip()

    try:
        producto = Producto(
            codigo,
            nombre,
            precio,
            categoria
        )

        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")
            guardar_productos()
        else:
            print("Ya existe un producto con ese código.")

    except ValueError as error:
        print(f"No se pudo registrar el producto: {error}")


def registrar_bebida() -> None:
    print("\n--- REGISTRAR BEBIDA ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    precio = leer_precio("Precio: $")
    categoria = input("Categoría: ").strip()
    tamanio = input("Tamaño: ").strip()

    try:
        bebida = Bebida(
            codigo,
            nombre,
            precio,
            categoria,
            tamanio
        )

        if restaurante.registrar_producto(bebida):
            print("Bebida registrada correctamente.")
            guardar_productos()
        else:
            print("Ya existe un producto con ese código.")

    except ValueError as error:
        print(f"No se pudo registrar la bebida: {error}")


def registrar_usuario() -> None:
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    if not identificacion or not nombre or not correo:
        print("Todos los datos son obligatorios.")
        return

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print(
            "Ya existe un usuario con esa identificación."
        )


def buscar_producto() -> None:
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código: ").strip()
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print("\nProducto encontrado:")
    producto.mostrar_informacion()


def actualizar_producto() -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Código del producto: ").strip()

    if restaurante.buscar_producto(codigo) is None:
        print("Producto no encontrado.")
        return

    nuevo_nombre = input("Nuevo nombre: ").strip()
    nuevo_precio = leer_precio("Nuevo precio: $")
    nueva_categoria = input(
        "Nueva categoría: "
    ).strip()

    if not nuevo_nombre or not nueva_categoria:
        print(
            "El nombre y la categoría son obligatorios."
        )
        return

    try:
        if restaurante.actualizar_producto(
            codigo,
            nuevo_nombre,
            nuevo_precio,
            nueva_categoria
        ):
            print("Producto actualizado correctamente.")
            guardar_productos()

    except ValueError as error:
        print(f"No se pudo actualizar: {error}")


def eliminar_producto() -> None:
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Código del producto: ").strip()

    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
        guardar_productos()
    else:
        print("Producto no encontrado.")


def listar_productos() -> None:
    print("\n--- LISTA DE PRODUCTOS ---")
    restaurante.listar_productos()


def mostrar_categorias() -> None:
    print("\n--- CATEGORÍAS REGISTRADAS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No hay categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def listar_usuarios() -> None:
    print("\n--- LISTA DE USUARIOS ---")
    restaurante.listar_usuarios()


def salir() -> None:
    print("Programa finalizado.")


ACCIONES_MENU = {
    "1": registrar_producto,
    "2": registrar_bebida,
    "3": registrar_usuario,
    "4": buscar_producto,
    "5": actualizar_producto,
    "6": eliminar_producto,
    "7": listar_productos,
    "8": mostrar_categorias,
    "9": listar_usuarios,
    "10": salir
}


def mostrar_menu() -> None:
    print("\n===== SISTEMA DEL RESTAURANTE =====")

    for numero, opcion in enumerate(
        OPCIONES_MENU,
        start=1
    ):
        print(f"{numero}. {opcion}")


def ejecutar_programa() -> None:
    while True:
        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        ).strip()

        accion = ACCIONES_MENU.get(opcion)

        if accion is None:
            print(
                "Opción incorrecta. Intente nuevamente."
            )
            continue

        accion()

        if opcion == "10":
            break


if __name__ == "__main__":
    ejecutar_programa()