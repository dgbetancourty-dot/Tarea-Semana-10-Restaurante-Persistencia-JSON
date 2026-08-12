# Tarea Semana 9 - Evolución del sistema de restaurante

## Estudiante

**Nombre:** Dennis Betancourt
**Asignatura:** Programación Orientada a Objetos
**Carrera:** Ingeniería en Tecnologías de la Información y Comunicación
**Paralelo:** A

## Descripción

Este proyecto es una evolución del sistema de restaurante desarrollado en las semanas anteriores. En esta versión se incorporan nuevas operaciones para administrar productos y usuarios, manteniendo una estructura modular y aplicando los conceptos estudiados en Programación Orientada a Objetos.

El sistema funciona mediante un menú interactivo en consola y permite registrar, buscar, actualizar, eliminar y listar productos. También permite registrar usuarios y mostrar las categorías existentes sin repetirlas.

## Estructura del proyecto

```text
Tarea-Restaurante App/
├── README.md
└── restaurante_app/
    ├── main.py
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   ├── bebida.py
    │   └── usuario.py
    └── servicios/
        ├── __init__.py
        └── restaurante.py
```

## Clases principales

### Producto

Representa los productos del restaurante y contiene los siguientes atributos:

* Código.
* Nombre.
* Precio.
* Categoría.

Sus atributos se mantienen encapsulados y pueden consultarse o modificarse mediante propiedades y setters.

### Bebida

Hereda de la clase `Producto` y agrega el atributo tamaño. De esta manera se reutilizan los atributos y métodos definidos en la clase principal.

### Usuario

Representa a las personas registradas en el sistema y contiene:

* Identificación.
* Nombre.
* Correo electrónico.

### Restaurante

Se encarga de administrar las colecciones de productos y usuarios. En esta clase se encuentra la lógica necesaria para registrar, buscar, actualizar, eliminar y listar información.

## Funcionalidades

El sistema permite realizar las siguientes operaciones:

1. Registrar productos.
2. Registrar bebidas.
3. Registrar usuarios.
4. Buscar productos por código.
5. Actualizar productos.
6. Eliminar productos.
7. Listar todos los productos.
8. Mostrar categorías sin elementos repetidos.
9. Listar todos los usuarios.
10. Finalizar el programa.

También se controla que no se registren productos con códigos repetidos ni usuarios con identificaciones duplicadas.

## Estructuras de datos utilizadas

Durante el desarrollo se utilizaron las siguientes estructuras:

### Listas

Se utilizan para almacenar los productos y usuarios registrados en el restaurante.

```python
self._productos: list[Producto] = []
self._usuarios: list[Usuario] = []
```

### Tupla

Se utiliza para guardar las opciones estables del menú, debido a que estas no necesitan modificarse durante la ejecución.

```python
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
```

### Diccionario

Relaciona cada opción del menú con la función que debe ejecutarse.

```python
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
```

### Conjunto

Se utiliza para obtener las categorías de los productos sin repetir valores.

```python
categorias = {
    producto.categoria
    for producto in self._productos
}
```

## Validaciones incorporadas

El programa incluye las siguientes validaciones:

* No permite códigos de productos duplicados.
* No permite identificaciones de usuarios repetidas.
* Verifica que los campos obligatorios no estén vacíos.
* Controla que el precio sea un valor numérico mayor que cero.
* Permite ingresar precios utilizando punto o coma decimal.
* Muestra un mensaje cuando un producto no existe.
* Controla las opciones incorrectas del menú.

## Anotaciones de tipos

Se utilizaron anotaciones de tipos en atributos, parámetros y valores de retorno para mejorar la claridad y facilitar la comprensión del código.

Ejemplo:

```python
def buscar_producto(self, codigo: str) -> Producto | None:
```

## Ejecución del programa

Se requiere Python 3.10 o una versión superior.

Desde PowerShell o la terminal, ingresar a la carpeta del proyecto:

```powershell
cd restaurante_app
```

Después ejecutar:

```powershell
python main.py
```

Al iniciar, se mostrará el menú principal del sistema.

## Pruebas realizadas

Se verificó correctamente:

* El registro de productos y bebidas.
* El control de códigos duplicados.
* El registro de usuarios.
* El control de identificaciones duplicadas.
* La búsqueda de productos.
* La actualización de nombre, precio y categoría.
* La eliminación de productos.
* El listado de productos y usuarios.
* La presentación de categorías sin duplicados.
* La validación de precios incorrectos.
* El control de opciones no válidas.

## Reflexión

Con esta actividad comprendí que las listas, tuplas, diccionarios y conjuntos tienen diferentes utilidades dentro de un programa. Las listas permiten almacenar varios objetos, las tuplas sirven para mantener datos que no deben cambiar, los diccionarios ayudan a relacionar opciones con acciones y los conjuntos permiten eliminar elementos repetidos.

También aprendí que organizar el programa en modelos, servicios y funciones facilita su comprensión y permite agregar nuevas funcionalidades sin tener que comenzar nuevamente todo el proyecto.
