class Cliente:
    def __init__(self, identificacion, nombre):
        self._identificacion = identificacion
        self._nombre = nombre

    @property
    def identificacion(self):
        return self._identificacion

    @property
    def nombre(self):
        return self._nombre

    def mostrar_informacion(self):
        print(f"Identificación: {self._identificacion}")
        print(f"Nombre: {self._nombre}")