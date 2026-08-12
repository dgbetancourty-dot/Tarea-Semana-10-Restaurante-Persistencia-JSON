from modelos.producto import Producto


class Bebida(Producto):
    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        categoria: str,
        tamanio: str
    ):
        super().__init__(codigo, nombre, precio, categoria)
        self._tamanio = tamanio

    @property
    def tamanio(self) -> str:
        return self._tamanio

    @tamanio.setter
    def tamanio(self, nuevo_tamanio: str) -> None:
        self._tamanio = nuevo_tamanio

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print(f"Tamaño: {self._tamanio}")