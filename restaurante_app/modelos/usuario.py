class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        self._identificacion = identificacion
        self._nombre = nombre
        self._correo = correo

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    def mostrar_informacion(self) -> None:
        print(f"Identificación: {self._identificacion}")
        print(f"Nombre: {self._nombre}")
        print(f"Correo: {self._correo}")
        