import json

from modelos.producto import Producto
from modelos.bebida import Bebida


class ArchivoServicio:
    def __init__(self, ruta_archivo: str) -> None:
        self._ruta_archivo = ruta_archivo

    def cargar_productos(self) -> list[Producto]:
        lista_productos = []

        try:
            with open(
                self._ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:
                registros_guardados = json.load(archivo)

            if not isinstance(registros_guardados, list):
                raise ValueError(
                    "El archivo JSON debe contener una lista."
                )

            for numero, registro in enumerate(
                registros_guardados,
                start=1
            ):
                try:
                    codigo = registro["codigo"]
                    nombre = registro["nombre"]
                    precio = registro["precio"]
                    categoria = registro["categoria"]
                    tipo = registro.get("tipo", "producto")

                    if not isinstance(codigo, str):
                        raise ValueError(
                            "El código debe ser un texto."
                        )

                    if not isinstance(nombre, str):
                        raise ValueError(
                            "El nombre debe ser un texto."
                        )

                    if not isinstance(precio, (int, float)):
                        raise ValueError(
                            "El precio debe ser numérico."
                        )

                    if not isinstance(categoria, str):
                        raise ValueError(
                            "La categoría debe ser un texto."
                        )

                    if tipo == "bebida":
                        tamanio = registro["tamanio"]

                        if not isinstance(tamanio, str):
                            raise ValueError(
                                "El tamaño debe ser un texto."
                            )

                        producto = Bebida(
                            codigo,
                            nombre,
                            precio,
                            categoria,
                            tamanio
                        )
                    else:
                        producto = Producto(
                            codigo,
                            nombre,
                            precio,
                            categoria
                        )

                    lista_productos.append(producto)

                except KeyError as error:
                    print(
                        f"Registro {numero} incompleto. "
                        f"Falta la clave: {error}."
                    )

                except (ValueError, TypeError) as error:
                    print(
                        f"Registro {numero} inválido: {error}"
                    )

        except FileNotFoundError:
            print(
                "El archivo productos.json no existe. "
                "El programa iniciará sin productos."
            )

        except json.JSONDecodeError:
            print(
                "El archivo productos.json no contiene "
                "un formato JSON válido."
            )

        except PermissionError:
            print(
                "No existen permisos para leer "
                "productos.json."
            )

        except ValueError as error:
            print(error)

        return lista_productos

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> bool:
        registros_productos = []

        for producto in productos:
            registros_productos.append(
                producto.a_diccionario()
            )

        try:
            with open(
                self._ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    registros_productos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:
            print(
                "No existen permisos para escribir "
                "en productos.json."
            )
            return False

        except FileNotFoundError:
            print(
                "No se encontró la carpeta donde debe "
                "guardarse productos.json."
            )
            return False