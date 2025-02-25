import sqlite3
import os 

DATABASE = 'tienda.db'

class Carro:
    def __init__(self):
        self.items = {} #{nombre:()}

    def agregar(self, item):
        if item.nombre in self.items:
            self.items[item.nombre][1] += item.cantidad
        else:
            self.items[item.nombre] = (item, item.cantidad)
        print(self.items)

    def remover(self, item):
        if item.nombre in self.items:
            self.items[item.nombre][1] -= item.cantidad
            if self.items[item.nombre][1] <= 0:
                del self.items[item]

    def total(self) -> float:
        """Calcula el total de la compra teniendo en cuenta cantidades"""
        return sum(producto.precio * cantidad for producto, cantidad in self.items.values())

    
    def vaciar(self):
        self.items = {}

    def pagar(self):
        """Vacia el carro y actualiza el stock de los productos en la base de datos"""
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        for producto, cantidad in self.items.values():
            c.execute("SELECT stock FROM productos WHERE id = ?", (producto.id,))
            stock_actual = c.fetchone()[0]

            if stock_actual < cantidad:
                print(f"No hay stock suficiente para {producto.nombre}")
                continue

            c.execute(
                "UPDATE productos SET stock = stock - ? WHERE id = ?", (cantidad, producto.id)
            )

        conn.commit()
        conn.close()
        self.vaciar()

    
    def __str__(self):
        return f"Carro: {self.items}"

class Producto:
    def __init__(self, filtro: str | int, cantidad: int):
        self.id, self.nombre, self.precio, self.stock = self.__get_info(filtro)
        self.cantidad = cantidad

    def __get_info(self, filtro)-> tuple[int, str, float, int]:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        if isinstance(filtro, int):
            c.execute("SELECT id, nombre, precio, stock FROM productos WHERE id = ?", (filtro,))
        else:
            c.execute("SELECT id, nombre, precio, stock FROM productos WHERE nombre = ?", (filtro,))
        
        data = c.fetchone()
        conn.close()

        if data is None:
            raise ValueError(f"Producto no encontrado: {filtro}")

        return data

    def __str__(self):
        return f"Producto: {self.nombre}, precio: {self.precio}, stock: {self.stock}"

    def __repr__(self):
        return f"Producto: {self.nombre}, precio: {self.precio}, stock: {self.stock}"

def create_db() -> None:
    """Crea la base de datos si no existe"""
    if os.path.exists(DATABASE):
        return
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE,
            precio REAL,
            stock INTEGER
        )
    """)
    conn.commit()
    valores = [
        (1, "Laptop", 800.0, 5),
        (2, "Mouse", 25.0, 20),
        (3, "Teclado", 50.0, 10),
        (4, "Monitor", 150.75, 8),
        (5, "Impresora", 120.0, 6),
        (6, "Auriculares", 35.5, 15),
        (7, "Cámara Web", 70.0, 12),
        (8, "Disco Duro", 100.0, 7),
        (9, "Memoria USB", 15.0, 30),
        (10, "Cargador Universal", 40.0, 10)
    ]
    c.executemany("INSERT INTO productos VALUES(?, ?, ?, ?)", valores)
    conn.commit()
    conn.close()

def get_productos() -> list[tuple[str, float, int]]:
    """Obtiene todos los productos de la base de datos"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT nombre, precio, stock FROM productos")
    productos = c.fetchall()
    conn.close()
    return productos

# Ejemplo de uso
create_db()
if __name__ == "__main__":
    a = Producto("Laptop", 1)
    print(a)
    carr = Carro()
    carr.agregar(a)
    print(carr.total(), carr)
