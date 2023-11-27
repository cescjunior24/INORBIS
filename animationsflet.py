import flet as ft

def main(page: ft.Page):


    #animate position fa que vagi més rapid o més lent 
    c1 = ft.Container(width=50, height=50, bgcolor="red", animate_position=2000)

    c2 = ft.Container(
        width=50, height=50, bgcolor="green", top=60, left=0, animate_position=2000
    )

    c3 = ft.Container(
        width=50, height=50, bgcolor="blue", top=120, left=0, animate_position=2000
    )

    def animate_container(e):
        #c1.top=20
        c1.left=200
        # c2.top = 100
        # c2.left = 40
        # c3.top = 180
        # c3.left = 100
        page.update()
    def animate_container_rewind(e):
        # c1.top = 0
        # c1.left = 200
        # c2.top = 60
        # c2.left = 0
        # c3.top = 120
        # c3.left = 0
        page.update()

    page.add(
        ft.Stack([c1, c2, c3], height=250),
        ft.ElevatedButton("Animate!", on_click=animate_container),
        ft.ElevatedButton("Animate Rewind!", on_click=animate_container_rewind)
    )

ft.app(target=main)