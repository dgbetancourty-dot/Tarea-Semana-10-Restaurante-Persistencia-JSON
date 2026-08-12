class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        categoria: str
    ):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._categoria = categoria

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        self._precio = nuevo_precio

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str) -> None:
        self._categoria = nueva_categoria

    def mostrar_informacion(self) -> None:
        print(f"Código: {self._codigo}")
        print(f"Nombre: {self._nombre}")
        print(f"Precio: ${self._precio:.2f}")
        print(f"Categoría: {self._categoria}")