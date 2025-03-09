## Funcion principal

* Tener diferentes objetos con la capacidad de añadirlos a un carrito
* Poder pagar y simular el funcionamiento del pago

## Uso

1. Instalar flet pip install flet
2. Poner todos los archivos en la misma carpeta
3. Correr el archivo main.py

**Importante** no borrrar tienda.db


## Clases
### Carro
Representa el carrito de compras.

- **Atributos**:
    - `itmes` (dict): Contiene los productos añadidos.  
        - **Clave:** Nombre del producto.  
        - **Valor:** Lista con el objeto `Producto` y la cantidad (`int`).  
- **Métodos**:  
    - `agregar(producto, cantidad)`: Añade un producto al carrito.  
    - `eliminar(nombre)`: Elimina un producto del carrito.  
    - `total()`: Retorna el costo total de los productos.
    - `vaciar()`: Vacia el carro.
    - `pagar()`: Simula el pago.

### Producto
Representa un producto disponible en la tienda.  

- **Atributos**:  
    - `id` (int): Id unico de cada producto
    - `nombre` (str): Nombre del producto.  
    - `precio` (float): Precio del producto.  
    - `stock` (int): Cantida disponible en la tienda
    - `cantidad` (int): Cantida que coge el usuario
- **Metodos**:
    - `__get_info()`: Devuelve una tupla con todos los atributos en la base de datos


### Header
Encabezado de la interfaz gráfica.
- **Atributos**:
    -
- **Métodos**:
    - 
    
### CarritoHeader
Muestra la información del carrito en la interfaz.

### Item
Representa un producto en la lista de la tienda.

### Cuadrícula
Organiza visualmente los productos en la tienda.

### CarritoInterface
Interfaz que muestra el contenido del carrito.
