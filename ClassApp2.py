import flet as ft

class student:
     def __init__(self,name,surname,fav_food,school,city,fav_animals):
         self.name=name
         self.surname=surname
         self.fav_food=fav_food
         self.school=school
         self.city=city
         self.fav_animals=fav_animals
         
         
         
def main(page:ft.Page):
    page.title="ClassAPP"
    
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
                            ft.ElevatedButton("Oriol", on_click=lambda _: page.go("/Oriol")),
                            ft.ElevatedButton("Marc", on_click=lambda _: page.go("/Marc")),
                            ft.ElevatedButton("Rayan", on_click=lambda _: page.go("/Rayan")),
                            ft.ElevatedButton("Francesc", on_click=lambda _: page.go("/Francesc"))
                        ],
                        alignment="center"
                    ),
                    ft.Image(
                        src="InorbisGITCristina\INORBIS.jpg"
                    )
                ],
            )   
        )
        if page.route == "/Cristina":
            cristina=student(name="Cristina",surname="Prieto",fav_food="Truita de Patates sense ceba",school="EMT",city="Granollers",fav_animals="Tortuga")
            ViewStudent(page,cristina)
        elif page.route =="/Rayan":
            rayan=student(name="Rayan",surname="Boumaiz",fav_food="Kebab",school="Marta Estrada",city="Granollers/Canovelles",fav_animals="Lobos")
            ViewStudent(page,rayan)
        elif page.route == "/Oriol":
            
            ViewStudent(page,)
            
    page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
def ViewStudent(page:ft.Page, student:student):
    page.views.append(
        ft.View(
            page.route,
            [
                ft.AppBar(title=ft.Text("Cristina"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ft.Row(
                    controls=[
                        ft.Text(value=student.name,size=30,color="blue"),
                        ft.Text(value=student.surname,size=30,color="blue") 
                    ]
                    
                )
            ],
        )
    )    
    

ft.app(target=main)