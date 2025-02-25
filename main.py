from interfaz_base import *
from clases_control import *

import flet as ft

def main(page: ft.Page):
    carrito = []  # Lista para almacenar los productos agregados

    # Función para manejar la navegación
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            # Vista de la Tienda
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Text("🛒 Tienda", size=30, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton("Ver Carrito", on_click=lambda e: page.go("/carrito")),
                        ft.Divider(),
                        ft.Text("📦 Producto 1 - $10"),
                        ft.ElevatedButton("Agregar al carrito", on_click=lambda e: agregar_al_carrito("Producto 1 - $10")),
                        ft.Text("📦 Producto 2 - $15"),
                        ft.ElevatedButton("Agregar al carrito", on_click=lambda e: agregar_al_carrito("Producto 2 - $15")),
                    ],
                )
            )

        elif page.route == "/carrito":
            # Vista del Carrito
            page.views.append(
                ft.View(
                    "/carrito",
                    [
                        ft.Text("🛍️ Carrito de Compras", size=30, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton("Volver a la Tienda", on_click=lambda e: page.go("/")),
                        ft.Divider(),
                        ft.Column([ft.Text(item) for item in carrito]) if carrito else ft.Text("🛑 Carrito vacío"),
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
