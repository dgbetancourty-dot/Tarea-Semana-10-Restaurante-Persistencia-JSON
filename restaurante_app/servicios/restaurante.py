from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

    def cargar_productos(
        self,
        productos_guardados: list[Producto]
    ) -> None:
        for producto in productos_guardados:
            self.registrar_producto(producto)

    def obtener_productos(self) -> list[Producto]:
        return self._productos.copy()

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self._productos:
            if producto.codigo.lower() == codigo.lower():
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nuevo_precio: float,
        nueva_categoria: str
    ) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nuevo_nombre
        producto.precio = nuevo_precio
        producto.categoria = nueva_categoria
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def listar_productos(self) -> None:
        if not self._productos:
            print("No hay productos registrados.")
            return

        for producto in self._productos:
            producto.mostrar_informacion()
            print("-" * 30)

    def obtener_categorias(self) -> set[str]:
        categorias = {
            producto.categoria
            for producto in self._productos
        }
        return categorias

    def registrar_usuario(self, usuario: Usuario) -> bool:
        for usuario_registrado in self._usuarios:
            if (
                usuario_registrado.identificacion
                == usuario.identificacion
            ):
                return False

        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> None:
        if not self._usuarios:
            print("No hay usuarios registrados.")
            return

        for usuario in self._usuarios:
            usuario.mostrar_informacion()
            print("-" * 30)