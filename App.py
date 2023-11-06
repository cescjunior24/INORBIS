import flet as ft
import time as time

def main(page: ft.Page):
    t1=ft.Text(value="Francesc Gallego Palomo",color="red",size=40,italic=True)
    t2=ft.Text(value="Francesc Gallego Palomo",color="green",size=40)
    page.add(t1,t2)
    
    contador=ft.Text()
    contador.color="cyan"
    contador.size=60
    page.add(contador)
    for i in range(10):
        contador.value=f"Contador: {i}"
        page.update()
        time.sleep(1)
    pass

    
ft.app(target=main)