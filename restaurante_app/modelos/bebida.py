from modelos.producto import Producto


class Bebida(Producto):
    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        categoria: str,
        tamanio: str
    ) -> None:
        super().__init__(codigo, nombre, precio, categoria)

        if not tamanio.strip():
            raise ValueError("El tamaño no puede estar vacío.")

        self._tamanio = tamanio.strip()

    @property
    def tamanio(self) -> str:
        return self._tamanio

    @tamanio.setter
    def tamanio(self, nuevo_tamanio: str) -> None:
        if not nuevo_tamanio.strip():
            raise ValueError("El tamaño no puede estar vacío.")

        self._tamanio = nuevo_tamanio.strip()

    def a_diccionario(self) -> dict:
        datos_bebida = super().a_diccionario()
        datos_bebida["tipo"] = "bebida"
        datos_bebida["tamanio"] = self._tamanio
        return datos_bebida

    def mostrar_informacion(self) -> None:
        super().mostrar_informacion()
        print(f"Tamaño: {self._tamanio}")