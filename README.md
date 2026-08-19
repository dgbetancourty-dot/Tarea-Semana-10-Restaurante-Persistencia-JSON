# Tarea Semana 10 - Persistencia de productos en JSON

## Datos del estudiante

**Nombre:** DENNIS BETANCOURT  
**Asignatura:** Programación Orientada a Objetos  
**Carrera:** Ingeniería en Tecnologías de la Información y Comunicación  
**Paralelo:** A  

## Descripción

Este proyecto corresponde a la evolución del sistema de restaurante desarrollado durante las semanas anteriores. En la Semana 10 se incorporó el manejo de archivos, el control de excepciones y la persistencia de productos mediante un archivo JSON.

El programa permite conservar los productos registrados después de cerrar la aplicación. Cuando el sistema se ejecuta nuevamente, los datos almacenados en `productos.json` se recuperan y se convierten otra vez en objetos de la clase `Producto` o `Bebida`.

La persistencia se aplica únicamente a los productos y bebidas. Los usuarios permanecen almacenados temporalmente en memoria, como indican las instrucciones de la actividad.

## Estructura del proyecto

```text
Tarea-Semana-10-Restaurante-Persistencia-JSON/
├── README.md
└── restaurante_app/
    ├── datos/
    │   └── productos.json
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   ├── bebida.py
    │   └── usuario.py
    ├── servicios/
    │   ├── __init__.py
    │   ├── archivo_servicio.py
    │   └── restaurante.py
    └── main.py
```

## Responsabilidad de los componentes

### Producto

La clase `Producto` representa los productos del restaurante. Contiene código, nombre, precio y categoría.

También realiza validaciones para impedir códigos, nombres o categorías vacías y precios menores o iguales a cero. El método `a_diccionario()` convierte el objeto en un diccionario compatible con JSON.

### Bebida

La clase `Bebida` hereda de `Producto` y agrega el atributo tamaño. También convierte su información en un diccionario para conservar el tamaño dentro del archivo JSON.

### Usuario

La clase `Usuario` representa a las personas registradas en el sistema. Contiene identificación, nombre y correo electrónico. En esta semana los usuarios permanecen únicamente en memoria.

### Restaurante

La clase `Restaurante` administra las colecciones de productos y usuarios. Se encarga de registrar, buscar, actualizar, eliminar y listar los productos, además de registrar y listar usuarios.

`main.py` no modifica directamente las listas internas de este servicio.

### ArchivoServicio

La clase `ArchivoServicio` se encarga únicamente de la persistencia. Utiliza `with open()`, codificación UTF-8, `json.load()` y `json.dump()` para cargar y guardar los productos.

También reconstruye los objetos `Producto` y `Bebida` a partir de los registros válidos recuperados desde el archivo JSON.

### main.py

Es el punto de inicio del programa. Presenta el menú, solicita los datos mediante `input()`, coordina las operaciones del restaurante y solicita el guardado después de registrar, actualizar o eliminar un producto.

## Funcionalidades

El sistema permite:

1. Registrar productos.
2. Registrar bebidas.
3. Registrar usuarios.
4. Buscar productos por código.
5. Actualizar productos.
6. Eliminar productos.
7. Listar productos.
8. Mostrar categorías sin repetirlas.
9. Listar usuarios.
10. Salir del programa.

## Funcionamiento de productos.json

El archivo `datos/productos.json` almacena la colección de productos como una lista de diccionarios.

Ejemplo:

```json
[
    {
        "codigo": "POO1",
        "nombre": "HAMBURGUESA",
        "precio": 4.5,
        "categoria": "COMIDA"
    }
]
```

Cuando se guarda una bebida, también se almacenan su tipo y tamaño para poder reconstruirla correctamente al iniciar nuevamente el programa.

Durante la ejecución, el sistema continúa trabajando con objetos. El archivo JSON se utiliza solamente para conservar y recuperar la información.

## Flujo de carga

1. Se inicia el programa desde `main.py`.
2. Se crea el servicio `ArchivoServicio`.
3. Se intenta abrir `datos/productos.json`.
4. `json.load()` recupera la lista de registros.
5. Cada registro es validado.
6. Los registros válidos se convierten nuevamente en objetos.
7. Los objetos son entregados al servicio `Restaurante`.
8. El menú trabaja normalmente con los productos recuperados.

## Flujo de guardado

1. El usuario registra, actualiza o elimina un producto.
2. `Restaurante` realiza la operación sobre la colección.
3. Los objetos se convierten en diccionarios.
4. `ArchivoServicio` utiliza `json.dump()`.
5. Se actualiza `datos/productos.json`.
6. Los cambios permanecen disponibles después de cerrar el programa.

## Excepciones controladas

El programa controla las siguientes excepciones:

- `FileNotFoundError`: permite iniciar con una colección vacía cuando `productos.json` todavía no existe.
- `json.JSONDecodeError`: controla un archivo que no posee un formato JSON válido.
- `PermissionError`: informa cuando no existen permisos para leer o escribir el archivo.
- `KeyError`: controla registros que no contienen alguna clave obligatoria.
- `ValueError`: controla productos con información inválida.
- `TypeError`: controla registros que contienen tipos de datos incorrectos.

No se utiliza `except: pass`, porque cada problema recibe una respuesta específica.

## Instrucciones de ejecución

Se requiere Python 3.10 o una versión superior.

Abrir PowerShell o la terminal de Visual Studio Code e ingresar a la carpeta de la aplicación:

```powershell
cd restaurante_app
```

Ejecutar:

```powershell
python main.py
```

Después se mostrará el menú principal del restaurante.

## Prueba de persistencia realizada

Para comprobar el funcionamiento se realizaron los siguientes pasos:

1. Se registró el producto `POO1`, con el nombre `HAMBURGUESA`, precio de `$3.50` y categoría `COMIDA`.
2. Se verificó que la información apareciera en `productos.json`.
3. Se cerró completamente el programa.
4. Se ejecutó nuevamente `main.py`.
5. Se listaron los productos y la hamburguesa fue recuperada correctamente.
6. Se actualizó su precio a `$4.50`.
7. Se reinició el programa y se comprobó que el nuevo precio permaneciera guardado.
8. Se registró una bebida con su tamaño y se comprobó que también se recuperara correctamente.
9. Se eliminó la bebida.
10. Se reinició nuevamente el programa y se confirmó que la eliminación también permaneciera guardada.

Estas pruebas demuestran que el registro, la actualización y la eliminación modifican correctamente el archivo JSON.

## Conclusión

Con esta actividad comprendí que las listas y los objetos almacenados en memoria desaparecen cuando el programa se cierra. Mediante un archivo JSON es posible conservar la información y recuperarla en una nueva ejecución.

También aprendí a utilizar excepciones específicas para evitar que errores esperados detengan completamente el programa y a mantener separada la lógica del restaurante del manejo de archivos.