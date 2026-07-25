# Sistema de Restaurante - Semana 8

## Estudiante

**Nombre: DENNIS BETANCOURT** 

## Descripción

Este proyecto corresponde a la actividad de la Semana 8 de la asignatura Programación Orientada a Objetos.

El sistema permite registrar productos, bebidas y clientes mediante un menú interactivo desarrollado en Python. El proyecto fue organizado utilizando una estructura modular y aplicando principios básicos SOLID.



## Estructura del proyecto

```
Tarea-Semana-8-Restaurante-SOLID
│
├── README.md
│
└── restaurante_app
    ├── main.py
    ├── modelos
    │   ├── __init__.py
    │   ├── producto.py
    │   ├── bebida.py
    │   └── cliente.py
    └── servicios
        ├── __init__.py
        └── restaurante.py
```

---

## Descripcion de cada clase

### Producto

Representa un producto general del restaurante.

### Bebida

Hereda de Producto y agrega el atributo tamaño.

### Cliente

Representa la información de un cliente.

### Restaurante

Administra el registro y listado de productos y clientes.

### main.py

Controla la interacción con el usuario mediante un menú por consola.

---

## Relación entre Producto y Bebida

La clase Bebida hereda de Producto porque una bebida representa un tipo específico de producto. Gracias a esta relación ambas clases pueden almacenarse en una misma colección y utilizar el método `mostrar_informacion()` mediante polimorfismo.



## Principios SOLID aplicados

### SRP (Responsabilidad Única)

Cada clase tiene una única responsabilidad.

### OCP (Abierto/Cerrado)

La clase Bebida amplía la funcionalidad del sistema sin modificar la clase Producto.

### LSP (Sustitución de Liskov)

Los objetos de tipo Bebida pueden utilizarse como objetos Producto sin afectar el funcionamiento del sistema.


## Ejecución

Ubicarse dentro de la carpeta `restaurante_app` y ejecutar:

```bash
python main.py
```


## Reflexión

Este proyecto me permitió poner en práctica los temas estudiados durante la unidad. Al principio tuve algunas dudas sobre cómo organizar las clases y relacionarlas entre sí, pero al avanzar entendí mejor el funcionamiento de la Programación Orientada a Objetos. Gracias a esta experiencia pude mejorar mi forma de programar y comprender la importancia de escribir un código organizado y fácil de mantener.