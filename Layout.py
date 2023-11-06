from cProfile import label
from typing import Text
import flet as ft


def main(page: ft.Page):

    nombre=ft.Text()
    label1=ft.TextField(label="Nombre")
    label2=ft.TextField(label="edad")
    
    
    def button_clicked(e):
        years=int(label2.value)
        if(years<18):
            text=ft.Text(value="Eres menor de edad")
        else:
            text=ft.Text(value="Eres mayor de edad")
        
        page.add(
        text
        )
            
        page.update()
            
        
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(
     ft.Row(controls=[
         ft.Text("A"),
         ft.Text("B"),
         ft.Text("C")
     ]),
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
     ]),
    ft.Row(controls=[
        label1,
        label2,
        b    
     ],
        alignment="center")
    )
    pass

ft.app(target=main)