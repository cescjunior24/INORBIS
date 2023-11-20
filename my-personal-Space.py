import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Cristina", on_click=lambda _: page.go("/Cristina")),
                    ft.ElevatedButton("Rayan", on_click=lambda _: page.go("/Rayan")),
                    ft.ElevatedButton("Oriol", on_click=lambda _: page.go("/Oriol")),
                    ft.ElevatedButton("Marc", on_click=lambda _: page.go("/Marc")),
                    ft.ElevatedButton("Jan", on_click=lambda _: page.go("/Jan")),
                    ft.ElevatedButton("Hadi", on_click=lambda _: page.go("/Hadi"))
                    
                ],
            )
        )
        if page.route == "/Cristina":
            page.views.append(
                ft.View(
                    "/Cristina",
                    [
                        ft.AppBar(title=ft.Text("Cristina"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)