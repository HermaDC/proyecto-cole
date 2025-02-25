import flet as ft
from clases_control import *

"""
Información importante:

* Para ejecutar hay que instalar flet `pip install flet`
* Para ejecutar hay que instalar sqlite3 `pip install sqlite3`
* Cada clase en este script y el otro sirve para algo y suele ser el nombre
* Si ves un `def main() -> str` significa que la función retorna un string
* Si tienes alguna duda puedes preguntar
* Los TODO ignoralos, son comentarios para mejorar cosas.
"""

# TODO: Agregar lógica del carrito
# TODO: Mejorar la UI
# TODO: Revisar añadir carrito


class Header(ft.AppBar):
    """Crea el appbar con el logo del carro"""

    def __init__(self, page, **kwargs):
        super().__init__(
            title=ft.Text("Mi Tienda Online"),
            center_title=True,
            bgcolor=ft.Colors.BLUE_200,
            actions=[
                ft.IconButton(ft.Icons.SHOPPING_CART, on_click=lambda e: self.root.go("/carrito")),
                ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda e: print("cerrar")),
            ],
            **kwargs
        )
        self.root = page
class CarritoHeader(Header):
    def __init__(self, page, **kwargs):
        super().__init__(page, **kwargs)
        self.title = ft.Text("Carrito")
        self.leading = ft.IconButton(ft.Icons.ARROW_BACK, on_click= lambda e: self.root.go("/"))

class Item(ft.Container):
    def __init__(self, nombre, precio, stock, page, carro, **kwargs):
        super().__init__(
            bgcolor="#a5a5a5",
            padding=5,
            border_radius=10,
            alignment=ft.alignment.center,
            **kwargs
        )

        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.root = page
        self.txt_number = ft.Text("0", size=20)
        self.carro = carro

        main = ft.Column(
            [
                ft.Image("https://via.placeholder.com/150", width=150, height=150),
                ft.Row(
                    [
                        ft.Text(self.nombre, size=25),
                        ft.Text(f"{self.precio}€", size=20, color=ft.Colors.GREEN_500),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ]
        )

        cantidad_intr = ft.Row(
            [
                ft.Row(
                    [
                        ft.IconButton(ft.Icons.REMOVE, on_click=self.minus_click),
                        self.txt_number,
                        ft.IconButton(ft.Icons.ADD, on_click=self.plus_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.IconButton(ft.Icons.SHOPPING_CART, on_click=self.add_to_cart),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        self.content = ft.Container(
            ft.Column(
                [main, cantidad_intr],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            padding=10,
            border_radius=10,
            width=250,
        )

    def minus_click(self, e):
        if int(self.txt_number.value or 0) < 1:
            return
        self.txt_number.value = str(int(self.txt_number.value or 0) - 1)
        self.root.update()

    def plus_click(self, e):
        self.txt_number.value = str(int(self.txt_number.value or 0) + 1)
        self.root.update()

    def add_to_cart(self, e):
        cantidad = self.txt_number.value
        if int(cantidad or 0) != 0:
            self.carro.agregar(Producto(self.nombre, int(cantidad or 0)))
            self.txt_number.value = "0"
            self.root.update()
            print("hecho")

class Cuadricula(ft.GridView):
    def __init__(self, **kwargs):
        super().__init__(
            expand=True,
            runs_count=3,
            spacing=10,
            run_spacing=10,
            **kwargs
        )

class CarritoInterface(ft.Container):
    def __init__(self, carro):
        super().__init__(
            bgcolor="#a5a5a5",
            padding=10,  # Agregamos un poco de padding para mejorar el diseño
        )

        rows: list[ft.Row] = []
        for product_name, obj_cant in carro.items.items():
            row = ft.Row([
                ft.Text(f"{product_name}", size=20, weight=ft.FontWeight.BOLD),
                ft.Text(f"Cantidad: {obj_cant[1]}"),
                ft.Text(f"Precio {obj_cant[0].precio * obj_cant[1]}€", color=ft.Colors.GREEN)
                #TODO añadir eliminar ft.IconButton()
            ], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            rows.append(row)

        # Encapsulamos en ft.Column
        self.content = ft.Column(rows, spacing=10)

def main(page: ft.Page):
    page.title = "Interfaz"
    page.appbar = Header(page)
    page.add(ft.Text("Bienvenido", size=40))

    # Crear cuadrícula
    cuadr = Cuadricula()
    page.add(cuadr)

    productos = get_productos()

    # Agregar productos
    for producto in productos:
        cuadr.controls.append(Item(producto[0], producto[1], producto[2], page, width=120, height=80))

    carro_inter = CarritoInterface(carro)
    page.add(carro_inter)
    # Actualizar la página
    page.update()

if __name__ == "__main__":
    carro = Carro()

    ft.app(target=main)
