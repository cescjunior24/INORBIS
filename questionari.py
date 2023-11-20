import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        page.clean()
        name=input_name.value
        age=int(input_age.value)
        text_nom=ft.Text(value=f"Hola {name}" )
        text_edat=ft.Text(value=f"Tens {age}")
        page.add(text_nom,text_edat)
        
    
    
    
    titulo=ft.Text(value="Qüestionari",size=40,color="blue")
    input_name=ft.TextField(label="Name",width=600)
    input_age=ft.TextField(label="Age")
    input_street=ft.TextField(label="Street")
    input_mail=ft.TextField(label="Mail")
    input_phone=ft.TextField(label="Phone")
    send_button=ft.ElevatedButton(text="Submit",on_click=button_clicked)
    page.add(
        ft.Row(
            controls=[titulo],
            alignment="center"
        ),
        ft.Row(
            controls=[input_name,input_age],
            alignment="center"
        ),
        ft.Row(
            controls=[send_button],
            alignment="center"
        )
    )
    pass

ft.app(target=main)