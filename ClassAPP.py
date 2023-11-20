import flet as ft

class Persona:
    def __init__(self ,name, age, height, school, lenguages):
        self.name = name
        self.age = age
        self.height= height
        self.school = school
        self.lenguages=lenguages

def main(page: ft.Page):
    page.title="Class APP"
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton("Cristina", on_click=lambda _: page.go("/Cristina")),
                            ft.ElevatedButton("Jan", on_click=lambda _: page.go("/Jan")),
                            ft.ElevatedButton("Oriol", on_click=lambda _: page.go("/Oriol")),
                            ft.ElevatedButton("Marc", on_click=lambda _: page.go("/Marc")),
                            ft.ElevatedButton("Eduardo", on_click=lambda _: page.go("/Eduardo")),
                            ft.ElevatedButton("Rayan", on_click=lambda _: page.go("/Rayan"))
                        ],
                        alignment="center"
                    ),
                    ft.Image(
                        src="/Users/francesc24/Desktop/INORBIS GIT/INORBIS/INORBIS.jpg"
                    )
                ],
            )
        )
        
        if(page.route=="/Cristina"):  
            alumno=Persona(name="Cristina",age=15,height=1.80,school="EMI",lenguages="Català, Castellà, English")
            ViewStudent(page,alumno)
        elif(page.route=="/Jan"):
            alumno=Persona(name="Jan",age=10,height=1.25,school="Educem",lenguages="Català, Castellà, English")
            ViewStudent(page,alumno)

    page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)




def ViewStudent(page:ft.Page, alumno:Persona):
        page.views.append(
        ft.View(
            page.route,
            [
                ft.AppBar(title=ft.Text(alumno.name), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ft.Row(
                    controls=[
                        ft.Text(value=alumno.age,size=30, color="blue")
                    ],
                    alignment="center"
                ),
                ft.Row(
                    controls=[
                            ft.Text(value=alumno.school,size=30, color="blue")
                    ],
                    alignment="center"      
                )
            ],
        )          
    )
ft.app(target=main)