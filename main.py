from interfaz_base import *
from clases_control import *

import flet as ft

carro = Carro()
def main(page: ft.Page):
    carrito = []  # Lista para almacenar los productos agregados

    # Función para manejar la navegación
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            # Vista de la Tienda
            cuadr = Cuadricula()
            productos = get_productos()

            # Agregar productos
            for producto in productos:
                cuadr.controls.append(Item(producto[0], producto[1], producto[2], page, width=120, height=80, carro=carro))

            page.views.append(
                ft.View(
                    "/",
                    [
                        Header(page), cuadr
                    ],
                )
            )

        elif page.route == "/carrito":
            # Vista del Carrito
            page.views.append(
                ft.View(
                    "/carrito",
                    [
                        CarritoHeader(page), CarritoInterface(carro)
                    ],
                )
            )

        page.update()

    # Función para agregar productos al carrito
    def agregar_al_carrito(producto):
        carrito.append(producto)
        page.update()

    page.on_route_change = route_change
    page.go("/")  # Cargar la vista inicial

ft.app(target=main)
